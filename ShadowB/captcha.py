import sys
import os
import random
import string
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    os.system(f"{sys.executable} -m pip install pillow")
    from PIL import Image, ImageDraw, ImageFont

def generate_captcha(cout,name=random.randint(1000,9999),path=""):
    if path and path not in [""," ","."]:
        output_filename = f"{path}\{name}.png"
        message = output_filename
    else:
        output_filename = f"{name}.png"
        message = output_filename
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(7))
    

    width, height = 250, 80
    background_color = (240, 240, 240)
    
   
    image = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    

    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()

    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line([(x1, y1), (x2, y2)], fill=line_color, width=2)
        
  
    for _ in range(500):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        pixel_color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
        draw.point((x, y), fill=pixel_color)

    
    current_x = 20
    for char in captcha_text:
       
        char_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        
        current_y = random.randint(15, 30)
        
        draw.text((current_x, current_y), char, fill=char_color, font=font)
       
        current_x += 30

 
    image.save(output_filename)
    
    print(f"[+] Captcha code generated successfully : '{message}'")
    if cout:
        print(f"[+] Captcha code : {captcha_text}")
    
    return captcha_text