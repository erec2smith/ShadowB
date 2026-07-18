import time
from ShadowB.Core.randwords import randw
from ShadowB.Core.fileorg import florg
try:
    from colorama import init, Fore, Style
except ImportError:
    import os
    os.system("pip install colorama")
    from colorama import init, Fore, Style


def start():
    init()
    while True:
        try:
            print(Fore.GREEN + "="*50 + Style.RESET_ALL)
            time.sleep(1)
            print(Fore.BLUE + "** welcome to ShadowBoys **" + Style.RESET_ALL)
            time.sleep(1)
            print("[1]. Generating random words")
            time.sleep(1)
            print("[2]. Organizing files")
            time.sleep(1)
            print("[3]. Exit")
            time.sleep(1)
            print(Fore.BLUE + "** Write here what you need, like 3 , 2 or 1 **" + Style.RESET_ALL)
            inp = input(">> ")
            if inp == "3":
                print(Fore.GREEN + f"** Closed ** \n {'='*50}" + Style.RESET_ALL)
                break
            
            elif inp == "1":
                others_chars = ""
                rep = int(input(Fore.RED + "** How many slots do you want to create? : " + Style.RESET_ALL))
                if rep > 5:
                    print(Fore.GREEN + "-- The maximum number of slots you can reach is 5 --" + Style.RESET_ALL)
                if rep < 2:
                    print(Fore.GREEN + "-- The smallest number of digits possible is 2 --" + Style.RESET_ALL)
                numbers = input(Fore.BLUE + "** Do you want to use numbers? (y/n) : " + Style.RESET_ALL)
                if numbers in ["n","no"]:
                    numbers = False
                else:
                    numbers = True
                symbols = input(Fore.BLUE + "** Do you want to use symbols? (y/n) : " + Style.RESET_ALL)
                if symbols in ["n","no"]:
                    symbols = False
                else:
                    symbols = True
                letters = input(Fore.BLUE + "** Do you want to use letters? (y/n) : " + Style.RESET_ALL)
                if letters in ["n","no"]:
                    letters = False
                else:
                    letters = True
                if letters:
                    form = input(Fore.BLUE + "** Do you want to use only uppercase letters (maj), only lowercase letters (min), or both uppercase and lowercase letters (all)? (min/maj/all) : " + Style.RESET_ALL)   
                else:
                    form = "none"
                filename = input(Fore.BLUE + "** Please write the name of the file where you will save the attempts (like pass or passwords)(only the name) : " + Style.RESET_ALL)
                if filename == "" or filename == " ":
                    filename = "core_generate"
                other_char = ""
                if letters or symbols:
                    other_char = input(Fore.BLUE + "** Do you have any special words, numbers, or dates you want to add? (y/n) : " + Style.RESET_ALL)
                    while not other_char in ["y","n"]:
                        other_char = input(Fore.BLUE + "** Do you have any special words, numbers, or dates you want to add? (y/n) : " + Style.RESET_ALL)
                    if other_char == "y":
                        n = int(input(Fore.BLUE + "** How many special words do you want to enter? : (1 or 10 or 88...)" + Style.RESET_ALL))
                        for i in range(n):
                            char = input(Fore.BLUE + f"** Enter the word number {i+1} : " + Style.RESET_ALL)
                            others_chars += char
                path = input(Fore.BLUE + rf"** Enter the path where you want to save the file, like (C:\Users\Username\Downloads), and if you want to store it in this path only, just put a dot (.) : " + Style.RESET_ALL)            
                randw(rep,numbers,symbols,letters,form,path,filename,others_chars)
                time.sleep(1)
                print(Fore.GREEN + "="*50 + Style.RESET_ALL)
                break
            
            elif inp == "2":
                path = input(Fore.BLUE + "** The folder path whose files we are going to organize: " + Style.RESET_ALL)
                florg(path)
                print("="*50)
                break
            else:
                print(Fore.RED + "-- They was an error, pls try again! --" + Style.RESET_ALL)
        except:
            print(Fore.RED + "-- They was an error, pls try again! --" + Style.RESET_ALL)
            break
        
def owner(cout=True):
    if cout:
        print(Fore.YELLOW + "Adem mzoughi" + Style.RESET_ALL)
        print(Fore.BLUE + "Github : https://github.com/erec2smith" + Style.RESET_ALL)
    return "Adem mzoughi"

def version(cout=True):
    if cout:
        print(Fore.GREEN + "1.5" + Style.RESET_ALL)
    return "1.5"
    
def team(cout=True):
    if cout:
        print(Fore.YELLOW + "Adem" + Style.RESET_ALL)
        print(Fore.GREEN + "Shadow" + Style.RESET_ALL)
        print(Fore.BLUE + "Berlin" + Style.RESET_ALL)
    return "Adem, Berlin, Shadow"

def help(cout=True):
    if cout:
        print(Fore.BLUE + "https://github.com/erec2smith/ShadowB" + Style.RESET_ALL)
    return "https://github.com/erec2smith/ShadowB"