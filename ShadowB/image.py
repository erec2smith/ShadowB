from ShadowB.Image.check_image import check 
from ShadowB.Image.export_metadata import exp
from ShadowB.Image.remove_metadata import remove
from ShadowB.Image.makeText import hide_text_in_img
from ShadowB.Image.makeFile import hide_file_in_img
from ShadowB.Image.extr_hidden_files import extract_file_from_img
from ShadowB.Image.extr_hidden_text import extract_text_from_img

def check_img(image):
    return check(image)


def expMetadata(image):
    return exp(image)


def removeMetadata(image):
    return remove(image)


def hide_text(image,text):
    return hide_text_in_img(image,text)

def hide_file(image,file):
    return hide_file_in_img(image,file)

def extr_file(image):
    return extract_file_from_img(image)

def extr_text(image):
    return extract_text_from_img(image)