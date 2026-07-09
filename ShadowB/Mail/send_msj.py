import smtplib
import re
import os
from email.mime.text import MIMEText

def send_email(sender, app_password, to, subject, body):
    content = body
    subtype = "plain"

    if os.path.isfile(body):
        ext = os.path.splitext(body)[1].lower()

        if ext in (".html", ".htm"):
            with open(body, "r", encoding="utf-8") as f:
                content = f.read()
            subtype = "html"

        elif ext == ".txt":
            with open(body, "r", encoding="utf-8") as f:
                content = f.read()
            subtype = "plain"

        else:
            with open(body, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            subtype = "plain"

    else:
        is_html = bool(re.search(r"<[a-zA-Z!][^>]*>", body))
        subtype = "html" if is_html else "plain"
        content = body

    msg = MIMEText(content, subtype)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_password)
            server.send_message(msg)
        print(200)
        return 200
    except Exception as e:
        print(404, e)
        return 404