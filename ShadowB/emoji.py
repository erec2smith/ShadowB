from random import choice as ch

def smile():
    return "\U0001F602"

def no_words():
    return "\U0001F642"

def birthday():
    return "\U0001F973"

def fire():
    return "\U0001F525"

def death():
    return "\u2620\ufe0f"

def coder():
    return "\U0001F9D1\U0001F3FB\u200D\U0001F4BB"

def skull():
    return "\U0001F480"

def heart():
    return "\U0001FAC0"

def sorry():
    return "\u2764\ufe0f\u200D\U0001FA79"

def love_u():
    return "\U0001F60D"

def crying():
    return "\U0001F62D"

def idk():
    return "\U0001F605"

def insult():
    return "\U0001F92C"

def random_emoji():
     emoji_list = [smile(),no_words(),birthday(),fire(),death(),coder(),skull(),heart(),sorry(),love_u(),crying(),idk(),insult()]
     emoji = ch(emoji_list)
     return emoji