import sys
import os
from pathlib import Path
try:
    import qrcode
except ImportError:
    os.system(f"{sys.executable} -m pip install qrcode[pil]")
    import qrcode
        
   

def qr(text, name, path):
    if path and path not in [""," ","."]:
        output_filename = f"{path}\{name}.png"
        message = output_filename
    else:
        output_filename = f"{name}.png"
        message = f"{Path.cwd()}\{output_filename}"
    try:
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=10, 
            border=4, 
        )
        
        
        qr.add_data(text)
        qr.make(fit=True)
        
       
        img = qr.make_image(fill_color="black", back_color="white")
        
       
        img.save(output_filename)
        
        print(f"[+] QRCode was generated successfully : '{message}'")
        
    except Exception as e:
        print(f"[-]  Error : {e}")
    return ""    