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
    
    
    
def _convert_to_degrees(value):
    try:
        degrees = float(value[0])
        minutes = float(value[1])
        seconds = float(value[2])
        return degrees + (minutes / 60.0) + (seconds / 3600.0)
    except Exception:
        return None

def exp(file_path):
   
    if not os.path.exists(file_path):
        return "File does not exist"
    
    
    try:
        with Image.open(file_path) as img:
          
            metadata = {
                "Filename": os.path.basename(file_path),
                "Format": img.format,
                "Dimensions": f"{img.width}x{img.height} pixels",
                "Mode": img.mode,
                "Capture_Date": "Unknown",      
                "Camera_Make": "Unknown",      
                "Camera_Model": "Unknown",     
                "Software": "Unknown",      
                "Location_GPS": "Unknown"     
            }
            
            
            exif_data = img._getexif()
            
            if exif_data is not None:
                gps_info = {}
                
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    
          
                    if tag_name == "DateTimeOriginal" or tag_name == "DateTime":
                        metadata["Capture_Date"] = str(value)
                    
                   
                    elif tag_name == "Make":
                        metadata["Camera_Make"] = str(value).strip()
                    elif tag_name == "Model":
                        metadata["Camera_Model"] = str(value).strip()
                    elif tag_name == "Software":
                        metadata["Software"] = str(value).strip()
                        
                  
                    elif tag_name == "GPSInfo":
                        for key in value:
                            sub_tag = GPSTAGS.get(key, key)
                            gps_info[sub_tag] = value[key]
                
                
                if gps_info and "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
                    lat = _convert_to_degrees(gps_info["GPSLatitude"])
                    lon = _convert_to_degrees(gps_info["GPSLongitude"])
                    
                  
                    if lat and gps_info.get("GPSLatitudeRef") == "S":
                        lat = -lat
                    if lon and gps_info.get("GPSLongitudeRef") == "W":
                        lon = -lon
                        
                    if lat and lon:
                   
                        metadata["Location_GPS"] = f"{lat:.6f}, {lon:.6f}"
            
            return metadata

    except (IOError, SyntaxError, Image.UnidentifiedImageError):
        return "This is not an image"
    