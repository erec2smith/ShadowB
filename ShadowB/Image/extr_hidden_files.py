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
    

def extract_file_from_img(image_path, output_directory="."):
    try:
        img = Image.open(image_path)
        decoded_data = stepic.decode(img)
        
        if not decoded_data:
            return "No hidden data found in this image"
            
        if isinstance(decoded_data, str):
            decoded_data = decoded_data.encode('utf-8')
            
        header_parts = decoded_data.split(b':', 2)
        if len(header_parts) < 3:
            return "Hidden data does not match the expected file format"
            
        file_name = header_parts[0].decode('utf-8')
        file_size = int(header_parts[1].decode('utf-8'))
        file_data = header_parts[2][:file_size]
        
        out_file_path = os.path.join(output_directory, file_name)
        with open(out_file_path, 'wb') as f:
            f.write(file_data)
            
        return f"File extracted successfully and saved as: {out_file_path}"
    except Exception as e:
        return f"An error occurred during extraction: {str(e)}"