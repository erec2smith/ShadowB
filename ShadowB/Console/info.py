try:
    from colorama import init, Fore, Style
except ImportError:
    import os
    os.system("pip install colorama")
    from colorama import init, Fore, Style
    
    
    
def inf(text):
    print(Fore.CYAN + "[*] " + text + Style.RESET_ALL)
