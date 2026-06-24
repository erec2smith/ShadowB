from ShadowB.Safe.filename import real_filename
from ShadowB.Safe.ext import real_ext
from ShadowB.Safe.cleanText import is_clean
from ShadowB.Safe.clean import cleann
from ShadowB.Safe.safeFile import is_safe
import os


def name(file):
    name = real_filename(file)
    return name


def ext(file):
    e = real_ext(file)
    return e


def extR(file):
    e = real_ext(file)
    return e.replace(".","")


def cleanText(text,check_list=None):
    if check_list and check_list is not None:
        clean = is_clean(text,check_list)
    else:
        clean = is_clean(text)
    if clean:
        print("true")
        return "true"
    else:
        print("false")
        return "false"



def clean(file,check_list=None):
    e = real_ext(file)
    if e not in ["pdf",".pdf",".txt","txt"]:
        print("Currently, the accepted files are .pdf and .txt")
        return "Currently, the accepted files are .pdf and .txt"
    
    
    if check_list and check_list is not None:
        c = cleann(file,check_list)
    else:
        c = cleann(file)
        
        
    if c:
        print("true")
        return "true"
    else:
        print("false")
        return "false"



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
    
    
def safeFile(file):
    safe = is_safe(file)
    if safe:
        print("true")
        return "true"
    else:
        print("false")
        return "false"