import os

try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except:
    import os
    os.system("pip install pillow")
    from PIL import Image
    from PIL.ExifTags import TAGS,GPSTAGS
    
    
    
try:
    import stepic
except:
    import os
    os.system("pip install stepic")
    import stepic
    
    

def check(image_path):
    if not image_path or not os.path.exists(image_path):
        return "No image provided or file does not exist"
        
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    if not image_path.lower().endswith(valid_extensions):
        return "We only accept images"
        
    try:
        img = Image.open(image_path)
        decoded_data = stepic.decode(img)
        
        if decoded_data:
            return "true"
        return "false"
    except:
        return "false"
