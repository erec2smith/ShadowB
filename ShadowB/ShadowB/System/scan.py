import socket
from concurrent.futures import ThreadPoolExecutor

data = []
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open!")
            data.append(port)
        s.close()
    except Exception:
        pass

def scan(target):
    print(f"Scanning target: {target}")
    print("Please wait, scanning in progress using multi-threading...")

    ports = range(1, 1125)
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda p: scan_port(target, p), ports)

    print("Scan completed!")
    return tuple(data) 
    
def get_ip_from_domainame(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return "Error: Invalid domain name or connection issue." 