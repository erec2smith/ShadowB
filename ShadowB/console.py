from ShadowB.Console.success import suc
from ShadowB.Console.info import inf
from ShadowB.Console.warning import wrg
from ShadowB.Console.error import err

def success(text):
    if not text:
        err("You need to enter text!")
    suc(text)
    
    
    
def info(text):
    if not text:
        err("You need to enter text!")
    inf(text)
    
    
def warning(text):
    if not text:
        err("You need to enter text!")
    wrg(text)
    
    
def error(text):
    if not text:
        err("You need to enter text!")
    err(text)    