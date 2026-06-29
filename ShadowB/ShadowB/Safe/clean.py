import os
import re
import ShadowB.Safe.cleanText
try:
    from pypdf import PdfReader
except:
    import os
    os.system("pip install pypdf")
    from pypdf import PdfReader

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

    check = cleanText.is_clean(normalized_text)
    if check:
        return True
    else:
        return False
    return False