import os

def real_ext(file):
    ext = os.path.splitext(file)[1].lower()
    return ext