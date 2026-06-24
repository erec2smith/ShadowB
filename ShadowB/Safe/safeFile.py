import os
import subprocess
import sys
import zipfile


def _ensure_package(import_name, pip_name=None):
    
    pip_name = pip_name or import_name
    try:
        return __import__(import_name)
    except ImportError:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install",
                 "--break-system-packages", pip_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception:
            return None
        try:
            return __import__(import_name)
        except ImportError:
            return None



magic = _ensure_package("magic", "python-magic")


pyclamd = _ensure_package("pyclamd", "pyclamd")


BLOCKED_EXTENSIONS = {
    "exe", "bat", "cmd", "apk", "cpp", "py", "js", "html",
    "css", "c", "java", "msi", "vbs", "ps1", "dll", "scr",
    "sh", "rb", "php", "pl", "go", "rs", "ts", "jar", "com",
    "pif", "reg", "hta", "wsf", "lnk"
}


EXECUTABLE_SIGNATURES = {
    b"MZ": "Windows PE/EXE",
    b"\x7fELF": "Linux ELF executable",
    b"\xfe\xed\xfa\xce": "Mach-O 32-bit executable",
    b"\xfe\xed\xfa\xcf": "Mach-O 64-bit executable",
    b"\xca\xfe\xba\xbe": "Mach-O fat binary / Java class",
}


EXECUTABLE_LIKE_EXTENSIONS = {"exe", "dll", "com", "scr", "msi"}

MAX_ZIP_DEPTH = 1                              
MAX_UNCOMPRESSED_SIZE = 200 * 1024 * 1024      
MAX_COMPRESSION_RATIO = 100                    

ZIP_BASED_EXTENSIONS = {"zip", "jar", "apk", "docx", "xlsx", "pptx"}


def _get_extension(file_path):
    return os.path.splitext(file_path)[1].lower().lstrip(".")


def _read_header(file_path, n=8):
    try:
        with open(file_path, "rb") as f:
            return f.read(n)
    except OSError:
        return b""


def _is_disguised_executable(file_path):
   
    header = _read_header(file_path, 8)
    ext = _get_extension(file_path)

    if ext in EXECUTABLE_LIKE_EXTENSIONS:
        return False  

    for sig in EXECUTABLE_SIGNATURES:
        if header.startswith(sig):
            return True
    return False


def _check_zip_bomb(file_path, depth=0):
 
    if depth > MAX_ZIP_DEPTH:
        return False

    try:
        with zipfile.ZipFile(file_path) as zf:
            total_uncompressed = 0
            for info in zf.infolist():
                total_uncompressed += info.file_size
                if total_uncompressed > MAX_UNCOMPRESSED_SIZE:
                    return False

                if info.compress_size > 0:
                    ratio = info.file_size / max(info.compress_size, 1)
                    if ratio > MAX_COMPRESSION_RATIO:
                        return False

                if info.filename.lower().endswith(".zip"):
                    if depth + 1 > MAX_ZIP_DEPTH:
                        return False
                    tmp_path = f"{file_path}.__nested_{depth}.tmp"
                    try:
                        with zf.open(info) as nested_file:
                            with open(tmp_path, "wb") as tmp:
                                tmp.write(nested_file.read())
                        nested_ok = _check_zip_bomb(tmp_path, depth + 1)
                        if not nested_ok:
                            return False
                    except (zipfile.BadZipFile, OSError):
                        return False
                    finally:
                        if os.path.exists(tmp_path):
                            os.remove(tmp_path)
    except zipfile.BadZipFile:
        return False 
    except OSError:
        return False

    return True


def _clamav_scan(file_path):
   
    if pyclamd is None:
        return None
    try:
        cd = pyclamd.ClamdUnixSocket()
        if not cd.ping():
            cd = pyclamd.ClamdNetworkSocket()
            cd.ping()
        result = cd.scan_file(file_path)
        return result is None  
    except Exception:
        return None


def is_safe(file):
   
    if not file or not os.path.isfile(file):
        return False

    ext = _get_extension(file)


    if ext in BLOCKED_EXTENSIONS:
        return False

   
    if _is_disguised_executable(file):
        return False

    
    header = _read_header(file, 4)
    looks_like_zip = header.startswith(b"PK\x03\x04") or ext in ZIP_BASED_EXTENSIONS
    if looks_like_zip:
        if not _check_zip_bomb(file):
            return False

    
    av_result = _clamav_scan(file)
    if av_result is False:
        return False

    return True