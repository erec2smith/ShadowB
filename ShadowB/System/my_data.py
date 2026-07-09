import getpass
import socket
import platform
import ctypes
import shutil
import requests
from .my_ip import get_ip

def make_file(filename,save=True):
 
    data = []
    data.append("=== Device Information ===\n")

    username = getpass.getuser()  
    data.append(f"Username: {username}\n")

    hostname = socket.gethostname()
    data.append(f"Hostname: {hostname}\n")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "Not available"
        
    url = f"http://ip-api.com/json/{get_ip(False)[1]}"
    response = requests.get(url)
    api_data = response.json()
    if api_data['status'] == 'success':
        country = api_data['country']
    else:
        country = "None"
        
    data.append(f"Local IP: {local_ip}\nCountry: {country}\n")

    os_name = platform.system()
    os_release = platform.release()
    arch = platform.architecture()[0]
    data.append(f"Operating System: {os_name} {os_release}\n")
    data.append(f"Architecture: {arch}\n")

    

    try:
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]
            def __init__(self):
                super(MEMORYSTATUSEX, self).__init__()
                self.dwLength = ctypes.sizeof(self)

        kernel32 = ctypes.windll.kernel32
        stat = MEMORYSTATUSEX()
        kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
        ram_bytes = stat.ullTotalPhys
        ram_mb = ram_bytes // (1024 * 1024)
        ram_gb = round(ram_mb / 1024, 1)
  
    except Exception as e:
        ram_gb, ram_mb = "N/A", "N/A"
       

    data.append(f"Total RAM: {ram_gb} GB  ({ram_mb} MB)\n")


    try:
       
        total, used, free = shutil.disk_usage('C:\\')
        total_gb = round(total / (1024**3), 1)
        used_gb = round(used / (1024**3), 1)
        free_gb = round(free / (1024**3), 1)
        
        data.append(f"Disk C: Total {total_gb} GB\n")
        data.append(f"Disk C: Used  {used_gb} GB\n")
        data.append(f"Disk C: Free  {free_gb} GB\n")
        
        info = (username, hostname, local_ip, country, os_name, os_release, arch, ram_gb, total_gb, used_gb, free_gb)
        
    except Exception as e:
        
        data.append(f"Disk C: Error reading usage - {str(e)}\n")
        info = (username, hostname, local_ip, country, os_name, os_release, arch, ram_gb, "Error", "Error", "Error")
    
    data.append("\n=== End of Information ===\n")
    if save:
        with open(f"{filename}.txt", "w", encoding="utf-8") as f:
            f.writelines(data)
        print(f"Saved at : {filename}.txt")    
        
    
    return info
