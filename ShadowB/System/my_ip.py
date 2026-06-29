import socket
import requests  

def get_country_free(ip_address=None):
    if not ip_address or ip_address.startswith(("192.168.", "10.", "172.")):
        url = "http://ip-api.com/json/?fields=status,message,country,query"
    else:
        url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if data.get("status") == "success":
            return {
                "ip": data.get("query"), 
                "country": data.get("country")
            }
        else:
            return {"ip": ip_address, "country": "Unknown", "error": data.get("message")}
            
    except requests.exceptions.RequestException:
        return {"ip": ip_address, "country": "Not available", "error": "Connection error"}


def get_ip(cout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = "Not available"

    
    geo_info = get_country_free() 
    
    public_ip = geo_info.get("ip", "Not available")
    country = geo_info.get("country", "Not available")
    
    if cout:
        print(f"Local IP  : {local_ip}")
        print(f"Public IP : {public_ip}")
        print(f"Country   : {country}")
    
    return (local_ip,public_ip,country)