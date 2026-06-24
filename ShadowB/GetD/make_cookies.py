import os
try:
    import browser_cookie3
except ImportError:
    import os
    os.system("pip install browser_cookie3")
    import browser_cookie3


def cookies(filename):
    cookies = browser_cookie3.chrome()


    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# This is a generated file! Do not edit.\n\n")
        
        for cookie in cookies:
       
            is_secure = "TRUE" if cookie.secure else "FALSE"
            expiration = str(int(cookie.expires)) if cookie.expires else "0"
            
            line = f"{cookie.domain}\t{is_secure}\t{cookie.path}\t{is_secure}\t{expiration}\t{cookie.name}\t{cookie.value}\n"
            f.write(line)
    
    print(f"Saved at : {filename}.txt and cookies") 
    return cookies