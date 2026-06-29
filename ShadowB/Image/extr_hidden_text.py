import os

try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except:
    os.system("pip install pillow")
    from PIL import Image
    from PIL.ExifTags import TAGS,GPSTAGS
    
    
try:
    import stepic
except:
    os.system("pip install stepic")
    import stepic


def extract_text_from_img(image_path):
    if not image_path or not os.path.exists(image_path):
        return "No image provided or file does not exist"
        
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    if not image_path.lower().endswith(valid_extensions):
        return "We only accept images"
        
    try:
        img = Image.open(image_path)
        decoded_data = stepic.decode(img)
        
        if not decoded_data:
            return "No hidden text found in this image"
            
        if isinstance(decoded_data, bytes):
            return decoded_data.decode('utf-8')
            
        return decoded_data
    except Exception as e:
        return f"An error occurred: {str(e)}"