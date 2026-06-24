import os

try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except:
    import os
    os.system("pip install pillow")
    from PIL import Image
    from PIL.ExifTags import TAGS,GPSTAGS


def remove(file_path, output_suffix="_cleaned"):
   
    if not os.path.exists(file_path):
        return "File does not exist"
    

    try:
        with Image.open(file_path) as img:
           
            file_dir, file_name = os.path.split(file_path)
            name, ext = os.path.splitext(file_name)
            
            
            new_file_name = f"{name}{output_suffix}{ext}"
            output_path = os.path.join(file_dir, new_file_name)
            
          
            cleaned_img = Image.new(img.mode, img.size)
            cleaned_img.putdata(img.getdata())
            
           
            cleaned_img.save(output_path, format=img.format)
            
  
            return {
                "Status": "Success",
                "Message": "Metadata removed successfully",
                "Original_File": file_name,
                "Cleaned_File": new_file_name,
                "Format": img.format,
                "Dimensions": f"{img.width}x{img.height} pixels"
            }

    except (IOError, SyntaxError, Image.UnidentifiedImageError):
       
        return "This is not an image"