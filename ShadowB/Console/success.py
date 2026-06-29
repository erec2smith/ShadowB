try:
    from colorama import init, Fore, Style
except ImportError:
    import os
    os.system("pip install colorama")
    from colorama import init, Fore, Style
    
    
    
def suc(text):
    print(Fore.GREEN + "[+] " + text + Style.RESET_ALL)