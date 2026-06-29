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


def hide_file_in_img(image_path, file_to_hide_path):
    if not image_path or not os.path.exists(image_path):
        return "No image provided or file does not exist"
        
    if not file_to_hide_path or not os.path.exists(file_to_hide_path):
        return "File to hide does not exist"
        
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    if not image_path.lower().endswith(valid_extensions):
        return "We only accept images"
        
    try:
        img = Image.open(image_path)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        file_name = os.path.basename(file_to_hide_path)
        with open(file_to_hide_path, 'rb') as f:
            file_data = f.read()
            
        header = f"{file_name}:{len(file_data)}:".encode('utf-8')
        payload = header + file_data
        
        encoded_img = stepic.encode(img, payload)
        
        img_dir, img_name = os.path.split(image_path)
        filename, _ = os.path.splitext(img_name)
        output_path = os.path.join(img_dir, f"{filename}_with_file.png")
        
        encoded_img.save(output_path, format='PNG')
        return f"Success! File hidden inside image. Saved at: {output_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"