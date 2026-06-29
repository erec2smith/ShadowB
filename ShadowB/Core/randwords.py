import string
from random import choice
import itertools as ito
from pathlib import Path


def randw(rep,numbers,symbols,letters,form,filename="core_generate",others_chars=""):
    if others_chars is None:
        others_chars = ""
    if numbers and symbols and letters:
        if form == "maj":
            final_combo = string.ascii_uppercase + string.digits + string.punctuation + others_chars
        elif form == "min":
            final_combo = string.ascii_lowercase + string.digits + string.punctuation + others_chars
        else:
            final_combo = string.ascii_letters + string.digits + string.punctuation + others_chars
           
           
    # numbers       
    elif numbers and symbols and not letters:
        final_combo =  string.digits + string.punctuation + others_chars

    elif numbers and not symbols and letters:
        if form == "maj":
            final_combo = string.ascii_uppercase + string.digits + others_chars
        elif form == "min":
            final_combo = string.ascii_lowercase + string.digits + others_chars
        else:
            final_combo = string.ascii_letters + string.digits + others_chars
        
    elif numbers and not symbols and not letters:
        final_combo = string.digits
        
        
    # letters    
    elif letters and symbols and not numbers:
        if form == "maj":
            final_combo = string.ascii_uppercase + string.punctuation + others_chars
        elif form == "min":
            final_combo = string.ascii_lowercase + string.punctuation + others_chars
        else:
            final_combo = string.ascii_letters + string.punctuation + others_chars
            
            
    elif letters and not symbols and not numbers:
        if form == "maj":
            final_combo = string.ascii_uppercase 
        elif form == "min":
            final_combo = string.ascii_lowercase 
        else:
            final_combo = string.ascii_letters
            
    
    #symbols
    elif symbols and not letters and not numbers:
        if form == "maj":
            final_combo = string.punctuation + others_chars
        elif form == "min":
            final_combo = string.punctuation + others_chars
        else:
            final_combo = string.punctuation + others_chars
            
    else:
        final_combo = string.ascii_letters + string.digits + string.punctuation + others_chars
    
    

    if rep > 5:
        print("The maximum number of slots you can reach is 5")
    if rep < 2:
        print("The smallest number of digits possible is 2")
    path = Path.cwd()
    words = [''.join(combo) for combo in ito.product(final_combo, repeat=rep)]
    with open(path / f"{filename}.txt","w") as w:
        for wr in words:
            w.write(wr + "\n")
        print(f"Alright, it has been saved in : {path / (filename + '.txt')}")        