import os
import re

try:
    from pypdf import PdfReader
except:
    import os
    os.system("pip install pypdf")
    from pypdf import PdfReader
    
try:
    from better_profanity import profanity
except ImportError:
    import os
    os.system("pip install better_profanity")
    from better_profanity import profanity

custom_bad_words = ["irheb","de3ch","israil","اسرائيل","trump","ارهاب","إرهاب","zab", "zebi", "asba","3asba","nyk","nayek","nik","nik omk","3asba lik","mnayek","fuck","shit","fuck you","fuck u","nik omo","t7chi fih","yatek asba","yatek 3asba","ya3tek 3asba","zok","omk","kiss","زبي","عصب","نيك","امك","برا نيك","يعطك عصبة","عصبة"]

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\u0600-\u06FF]', '', text)
    return text





def pdf_to_txt(file):
    try:
        if not file.lower().endswith(".pdf"):
            raise ValueError("Currently, the accepted files are .pdf and .txt")

        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    except Exception as e:
        print(e)
        return "error"
    
    
    
def txt_to_text(file):
    try:
        if not file.lower().endswith(".txt"):
            raise ValueError("Currently, the accepted files are .pdf and .txt")

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        return text

    except Exception as e:
        print(e)
        return "error"



def is_clean(text,check_list=None):
    if not text:
        print("Maybe there's a mistake, no text was received!")
        return False

    normalized_text = normalize(text)

    
    for word in custom_bad_words:
        if word in normalized_text:
            return False
        
    if check_list:
        for w in check_list:
            if w in normalized_text:
                return False 

  
    if profanity.contains_profanity(text):
        return False

    return True



def cleann(file,check_list=None):
    if not file:
        print("Maybe there's a mistake, no file was received!")
        return False
    
    
    
    if file.lower().endswith(".pdf"):
        text = pdf_to_txt(file)
        
    elif file.lower().endswith(".txt"):
        text = txt_to_text(file)
     
    else:
        print("Currently, the accepted files are .pdf and .txt")
        return "Currently, the accepted files are .pdf and .txt"
        
    if text == "error":
        print("An error occurred: Please try again, making sure the file is in PDF format and that it is a text document, not a scanned copy or image!")
        return False

    normalized_text = normalize(text)

    
    for word in custom_bad_words:
        if word in normalized_text:
            return False
        
    if check_list:
        for w in check_list:
            if w in normalized_text:
                return False 

  
    if profanity.contains_profanity(text):
        return False

    return True


