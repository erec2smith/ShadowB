import time
from ShadowB.Core.randwords import randw
from ShadowB.Core.fileorg import florg
try:
    from colorama import init, Fore
except ImportError:
    import os
    os.system("pip install colorama")
    from colorama import init, Fore


def start():
    init()
    while True:
        try:
            print(Fore.GREEN + "="*50)
            time.sleep(1)
            print(Fore.BLUE + "** welcome to ShadowBoys **")
            time.sleep(1)
            print("[1]. Generating random words")
            time.sleep(1)
            print("[2]. Organizing files")
            time.sleep(1)
            print("[3]. Exit")
            time.sleep(1)
            print(Fore.BLUE + "** Write here what you need, like 3 , 2 or 1 **")
            inp = input(">> ")
            if inp == "3":
                print(Fore.GREEN + f"** Closed ** \n {'='*50}")
                break
            
            elif inp == "1":
                others_chars = ""
                rep = int(input(Fore.RED + "** How many slots do you want to create? : "))
                if rep > 5:
                    print(Fore.GREEN + "-- The maximum number of slots you can reach is 5 --")
                if rep < 2:
                    print(Fore.GREEN + "-- The smallest number of digits possible is 2 --")
                numbers = input(Fore.BLUE + "** Do you want to use numbers? (y/n) : ")
                if numbers in ["n","no"]:
                    numbers = False
                else:
                    numbers = True
                symbols = input(Fore.BLUE + "** Do you want to use symbols? (y/n) : ")
                if symbols in ["n","no"]:
                    symbols = False
                else:
                    symbols = True
                letters = input(Fore.BLUE + "** Do you want to use letters? (y/n) : ")
                if letters in ["n","no"]:
                    letters = False
                else:
                    letters = True
                form = input(Fore.BLUE + "** Do you want to use only uppercase letters (maj), only lowercase letters (min), or both uppercase and lowercase letters (all)? (min/maj/all) : ")   
                filename = input(Fore.BLUE + "** Please write the name of the file where you will save the attempts (like pass or passwords)(only the name) : ")
                if filename == "" or filename == " ":
                    filename = "core_generate"
                other_char = ""
                if letters or symbols:
                    other_char = input(Fore.BLUE + "** Do you have any special words, numbers, or dates you want to add? (y/n) : ")
                    while not other_char in ["y","n"]:
                        other_char = input(Fore.BLUE + "** Do you have any special words, numbers, or dates you want to add? (y/n) : ")
                    if other_char == "y":
                        n = int(input(Fore.BLUE + "** How many special words do you want to enter? : (1 or 10 or 88...)"))
                        for i in range(n):
                            char = input(Fore.BLUE + f"** Enter the word number {i+1} : ")
                            others_chars += char
                randw(rep,numbers,symbols,letters,form,filename,others_chars)
                time.sleep(1)
                print(Fore.GREEN + "="*50)
                break
            
            elif inp == "2":
                path = input(Fore.BLUE + "** The folder path whose files we are going to organize: ")
                florg(path)
                print("="*50)
                break
            else:
                print(Fore.RED + "-- They was an error, pls try again! --")
        except:
            print(Fore.RED + "-- They was an error, pls try again! --")
            break
        
def owner():
    print(Fore.YELLOW + "Adem mzoughi")
    print(Fore.BLUE + "Github : https://github.com/erec2smith")

def vr():
    print(Fore.GREEN + "0.6")
    
def team():
    print(Fore.YELLOW + "Adem")
    print(Fore.GREEN + "Shadow")
    print(Fore.BLUE + "Berlin")

def hp():
    print(Fore.BLUE + "https://github.com/erec2smith/ShadowB")
    