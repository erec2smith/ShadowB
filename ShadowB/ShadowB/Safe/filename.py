import os

def real_filename(file):
    name = ext = os.path.splitext(os.path.basename(file))[0]
    return name
 