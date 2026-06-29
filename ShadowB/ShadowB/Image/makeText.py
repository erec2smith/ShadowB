import os

try:
    from PIL import Image
except:
    os.system("pip install pillow")
    from PIL import Image

try:
    import stepic
except:
    os.system("pip install stepic")
    import stepic
    

def hide_text_in_img(image_path, text):
    if not image_path or not os.path.exists(image_path):
        return "No image provided or file does not exist"
        
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    if not image_path.lower().endswith(valid_extensions):
        return "We only accept images"
        
    if not text:
        return "No text provided to hide"
        
    try:
        img = Image.open(image_path)
        
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        encoded_img = stepic.encode(img, text.encode('utf-8'))
        
        filename, ext = os.path.splitext(image_path)
        output_path = f"{filename}_hidden.png"
        
        encoded_img.save(output_path, format='PNG')
        return f"Success! Image saved at: {output_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"