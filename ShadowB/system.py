from ShadowB.System.my_data import make_file
from ShadowB.System.make_cookies import cookiees
from ShadowB.System.my_ip import get_ip
from ShadowB.System.scan import scan, get_ip_from_domainame
from pathlib import Path
import os
import requests as req
import time
from speedtest import Speedtest

def informations(filename="Device_informations",save=True):
    return make_file(save,filename)
    

def ip(cout=True):
    return get_ip(cout)


def cookies(filename="cookies"):
    return cookiees(filename)


def scan_open_ports(ip):
    return scan(ip)

def path():
    current_path = Path.cwd()
    return current_path

def domain_informations(domain):
    return get_ip_from_domainame(domain)


def remove_file(path):
    full_path = os.path.abspath(path)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return 200  
        except Exception as e:
            return 400 
    else:
        return 404
    
    
def spider(url):
    if not url:
        print("The link is required!")
        return 405
    available_paths = []
    paths = ["admin","ad","login","singup","signin","robots.txt","add","upload","home","index","register","check","code","view","admins","administrator","mod","mod1","mod2","mod3","admin1","admin2","admin3","log","file","files","boots","bot","chat","new","login-php","login-admin","admin-login","php_admin","php-login","admin-php","search","product","more","about","contact","products","project","account","accounts","profile","profiles","op","ap","app","sessoin","sessions","error","hide","setting","settings","solde","balance","amount","found","create","make","plus","pro","offer","offers","terms","msg","message","messages","dashboard","data","info","informations","information","v","version","history","conv","conversations","panel","admin-panel","film","films","movie","movies","target"]
    for path in paths:
        res = req.get(f"{url}/{path}")
        if res.status_code == 200:
            available_paths.append(f"/{path}")
            time.sleep(1)
             
    if len(available_paths) > 0:
        return available_paths
    else:
        return 404
    
    
def wifi_speed(cout=True):
    wifi = Speedtest()
    if cout:
        print("Download Speed...")
    download = wifi.download() / 1024 / 1024
    if cout:
        print(f"Download {download:.2f} Mbps")
    if cout:
        print("Upload speed...")
    upload = wifi.upload() / 1024 / 1024
    if cout:
        print(f"Upload {upload:.2f} Mbps")
    dwn = f"{download:.2f}"
    upld = f"{upload:.2f}"
    return (float(dwn),float(upld))    