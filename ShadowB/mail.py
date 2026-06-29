from ShadowB.Mail.make_mail import create_temp_email
from ShadowB.Mail.res_msj import get_messages
from ShadowB.Mail.send_msj import send_email

def create_email():
    return create_temp_email()


def get_msj(token):
    if token:
        return get_messages(token)
    else:
        return "Entering the token is mandatory!"
    
    
    
def send_msj(sender, app_password, to, subject, body):
    if sender and app_password and to and subject and body:
        return send_email(sender, app_password, to, subject, body)
    else:
        return "(sender, app_password, to, subject, body) must be entered compulsorily!"    