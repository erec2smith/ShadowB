from ShadowB.Image.check_image import check 
from ShadowB.Image.export_metadata import exp
from ShadowB.Image.remove_metadata import remove
from ShadowB.Image.makeText import hide_text_in_img
from ShadowB.Image.makeFile import hide_file_in_img
from ShadowB.Image.extr_hidden_files import extract_file_from_img
from ShadowB.Image.extr_hidden_text import extract_text_from_img

def has_hidden_data(image):
    return check(image)

def read_metadata(image):
    return exp(image)

def strip_metadata(image):
    return remove(image)

def embed_text(image,text):
    return hide_text_in_img(image,text)

def embed_file(image,file):
    return hide_file_in_img(image,file)

def extract_file(image):
    return extract_file_from_img(image)

def extract_text(image):
    return extract_text_from_img(image)