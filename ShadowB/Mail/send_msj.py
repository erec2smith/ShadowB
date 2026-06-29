import smtplib
import re
from email.mime.text import MIMEText


def send_email(sender, app_password, to, subject, body):
    is_html = bool(re.search(r"<[a-zA-Z!][^>]*>", body))
    subtype = "html" if is_html else "plain"
    msg = MIMEText(body, subtype)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_password)
            server.send_message(msg)
        print(200)    
        return 200
    except:
        print(404)
        return 404