import os
import re
try:
    from better_profanity import profanity
except ImportError:
    import os
    os.system("pip install better_profanity")
    from better_profanity import profanity

custom_bad_words = ["irheb","ass","dick","cock","asshole","de3ch","israil","اسرائيل","trump","ارهاب","إرهاب","zab", "zebi", "asba","3asba","nyk","nayek","nik","nik omk","3asba lik","mnayek","fuck","shit","fuck you","fuck u","nik omo","t7chi fih","yatek asba","yatek 3asba","ya3tek 3asba","zok","omk","kiss","زبي","عصب","نيك","امك","برا نيك","يعطك عصبة","عصبة"]

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\u0600-\u06FF]', '', text)
    return text

def is_clean(text,check_list=None):
    if not text:
        return True

    normalized_text = normalize(text)

    
    for word in custom_bad_words:
        if word in normalized_text:
            return False
        
    if check_list:
        for w in check_list:
            if w in normalized_text:
                return False 

  
    if profanity.contains_profanity(text):
        return False

    return True