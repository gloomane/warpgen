import random
import httpx
import os
import time
import requests
import datetime
from hashlib import md5

keys = requests.get(
    "https://raw.githubusercontent.com/gloomane/warpkeys/main/keys").content.decode().split(",")
if len(keys) == 0:
    print("Нет ключей для генерации!")
    exit()
gkeys = []
os.system('cls' if os.name == "nt" else 'clear')

print("\n█░█░█ ▄▀█ █▀█ █▀█ ▄█▄\n▀▄▀▄▀ █▀█ █▀▄ █▀▀ ░▀░\n")
print(
    't.me/xaltamy'
)

print()  


value_int = 999999999

a = 0

while a < value_int:
    a += 1
    print(datetime.datetime.now())

    try:
        # Заголовок с переменными
        headers = {
            "CF-Client-Version": "a-6.11-2223",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }

        with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223",
                          headers=headers,
                          timeout=30.0) as client:

            r = client.post("/reg")
            id = r.json()["id"]
            license = r.json()["account"]["license"]
            token = r.json()["token"]
            r = client.post("/reg")
            id2 = r.json()["id"]
            token2 = r.json()["token"]

            headers_get = {"Authorization": f"Bearer {token}"}
            headers_get2 = {"Authorization": f"Bearer {token2}"}
            headers_post = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token}",
            }

            json = {"referrer": f"{id2}"}
            client.patch(f"/reg/{id}", headers=headers_post, json=json)

            client.delete(f"/reg/{id2}", headers=headers_get2)

            key = random.choice(keys)

            json = {"license": f"{key}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            json = {"license": f"{license}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            r = client.get(f"/reg/{id}/account", headers=headers_get)
            account_type = r.json()["account_type"]
            referral_count = r.json()["referral_count"]
            license = r.json()["license"]

            client.delete(f"/reg/{id}", headers=headers_get)
            gkeys.append(license)
            if referral_count == 1:
                with open('gened1GB.txt','a') as f:
                    f.write(license + '\n')
                    print("1GB GENED")
            else:
                with open('gened12PB.txt','a') as f:
                    f.write(license + '\n')
                    print("12PB GENED")
                    print("Номер ключа:", a)
            

    except:
        print("Ошибка.")
        time.sleep(15)
    if a % 2 == 0:
        time.sleep(60)