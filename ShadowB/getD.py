from ShadowB.GetD.my_data import make_file
from ShadowB.GetD.make_cookies import cookies
from ShadowB.GetD.my_ip import ip
from ShadowB.GetD.scan import scan, get_ip_from_domainame
from pathlib import Path

def my_data(filename="Device_informations",save=True):
    return make_file(save,filename)
    



def my_ip(cout=True):
    return ip(cout)


def get_cookies(filename="cookies"):
    return cookies(filename)


def scan_open_ports(ip):
    return scan(ip)

def whm():
    current_path = Path.cwd()
    print(current_path)
    return current_path

def get_ip_from_domain(domain):
    return get_ip_from_domainame(domain)