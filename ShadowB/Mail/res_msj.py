try:
    import requests
except:
    import os
    os.system("pip install requests")
    import requests
import random
import string
import time
BASE_URL = "https://api.mail.tm"
def get_messages(token):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/messages", headers=headers)
    resp.raise_for_status()
    messages = resp.json()["hydra:member"]
    if not messages:
        return "There aren't any messages so far"
    result = []
    for msg in messages:
        msj_id = msg["id"]
        date = msg["createdAt"]
        sender = msg["from"]["address"]
        subject = msg["subject"]
        msj = get_message_details(token, msj_id)["intro"]
        result.append((msj_id, date, sender, subject, msj))
    return result
def get_message_details(token, message_id):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/messages/{message_id}", headers=headers)
    resp.raise_for_status()
    return resp.json()
def print_messages_separately(token):
    messages = get_messages(token)
    if isinstance(messages, str):
        print(messages)
        return
    for i, msg in enumerate(messages, start=1):
        msj_id, date, sender, subject, msj = msg
        print("=" * 50)
        print(f"msj #{i}")
        print(f"from        : {sender}")