from ShadowB.Safe.filename import real_filename
from ShadowB.Safe.ext import real_ext
from ShadowB.Safe.cleanText import is_clean
from ShadowB.Safe.clean import cleann
from ShadowB.Safe.safeFile import safe_file
from ShadowB.Console.error import err
import os


def name(file):
    name = real_filename(file)
    return name


def file_extension(file):
    e = real_ext(file)
    return e.replace(".","")


def validate_text(text,check_list=None):
    if check_list and check_list is not None:
        return is_clean(text,check_list)
    else:
        return is_clean(text)



def scan_file(file,check_list=None):
    e = real_ext(file)
    if e not in ["pdf",".pdf",".txt","txt"]:
        print("Currently, the accepted files are .pdf and .txt")
        return "Currently, the accepted files are .pdf and .txt"
    
    
    if check_list and check_list is not None:
        return cleann(file,check_list)
    else:
        return cleann(file)




def size(file):
    try:
        size_bytes = os.path.getsize(file)
        size_mb = size_bytes / (1024 * 1024)
        print(size_mb)
        return size_mb

    except Exception as e:
        print(e)
        print("error!")
        return "error!"
    
    
def is_safe(file):
    return safe_file(file)
    
    
    
def clean_text(text,mode="normal"):
    final_result = ""
    text1 = "".join(c for c in text if c.isalpha() or c.isspace())
    if mode  == "normal":
        final_result = text1
    elif mode == "upper":
        final_result = text1.upper()
    elif mode == "lower":
        final_result = text1.lower()
    elif mode == "capital":
        final_result = text1.title()    
    else:
        err(f"Invalid value : clean_text() does not contain mode = {mode} !")
    return final_result