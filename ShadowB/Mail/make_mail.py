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

def random_string(length=10):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def create_temp_email():
    domains_resp = requests.get(f"{BASE_URL}/domains")
    domains_resp.raise_for_status()
    domain = domains_resp.json()["hydra:member"][0]["domain"]
    username = random_string()
    password = random_string(14)
    address = f"{username}@{domain}"
    create_resp = requests.post(
        f"{BASE_URL}/accounts",
        json={"address": address, "password": password},
    )
    create_resp.raise_for_status()
    token_resp = requests.post(
        f"{BASE_URL}/token",
        json={"address": address, "password": password},
    )
    token_resp.raise_for_status()
    token = token_resp.json()["token"]
    return (address,password,token)