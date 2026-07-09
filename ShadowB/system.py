from ShadowB.System.my_data import make_file
from ShadowB.System.make_cookies import cookiees
from ShadowB.System.my_ip import get_ip
from ShadowB.System.scan import scan, get_ip_from_domainame
from pathlib import Path
import os

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
    