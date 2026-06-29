try:
    from colorama import init, Fore, Style
except ImportError:
    import os
    os.system("pip install colorama")
    from colorama import init, Fore, Style
    
    
    
def err(text):
    print(Fore.RED + "[-] " + text + Style.RESET_ALL)
