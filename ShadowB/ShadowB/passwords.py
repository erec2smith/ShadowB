import string
import secrets
import re


def create_password():
    length = 20
    all_characters = string.ascii_letters + string.punctuation + string.digits 
    

    password = "".join(secrets.choice(all_characters) for _ in range(length))
    
    return password



def check_strength(password):
    pass_list = ["azerty","azerty22","1234","google","insta","yamal","123456789","password","mot passe","abcdefghijklmnopqrstuvwxyz","pass123","password123","pass","password","ronaldo","cr7ronaldo","ronaldo2008","messi","fcmessi","itsme","hacker","azertyuiopmlkjhgfdsqwxcvbn","azertyuiopqsdfghjklmwxcvbn"]

    length_error = len(password) < 8
    

    lowercase_error = re.search(r"[a-z]", password) is None
    
   
    uppercase_error = re.search(r"[A-Z]", password) is None
    

    digit_error = re.search(r"\d", password) is None
    
   
    symbol_error = re.search(r"[ !@#$%^&*(),.?\":{}|<>_\-+=\[\]\\/`~;']", password) is None
    

    errors = [length_error, lowercase_error, uppercase_error, digit_error, symbol_error]
    passed_conditions = errors.count(False)
    
   
    if len(password) >= 12 and passed_conditions == 5 and password not in pass_list:
        print("Strong")
        return ""
    elif len(password) >= 8 and passed_conditions >= 3 and password not in pass_list:
        print("Medium")
        return ""
    else:
        print("Weak")
        return ""