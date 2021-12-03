import requests
import json
import random
import string
import pyfiglet
from time import sleep
from colorama import Fore, Back, Style

text = pyfiglet.figlet_format("SPAMMER" , font = "big")


def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def getMessage(pingQ):
    if pingQ == "y":
        if choice == "n":
            return "@everyone " + id_generator(1900)
        if choice == "y":
            return "@everyone " + input("Enter text: ")
    if pingQ == "n":
        if choice == "n":
            return id_generator(1900)
        if choice == "y":
            return input("Enter text: ")

def send_message(webhook_url, message):
    username = id_generator()
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": True
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)

    if not response.ok:
        if response.status_code == 429:
            print(Fore.RED+" << Ping : You are being rate limited")
        else:
            print(Fore.RED+" << Ping : Failed to send message")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        return False
    else:
        print(Fore.GREEN+f" << Ping : Successfully sent {sent_count} instances")
        return True

print(text)
print("discord: xq#0001")
print("TikTok:xq.on.top")

webhook = input("Webhook URL => ")
pingQ = input("Do you want mass pings : y/n => ")
choice = input("Do you want custom text : y/n => ")
message = getMessage(pingQ)
attempt_count = 0
sent_count = 1


failed_previous = False


try:
    while True:
        if (send_message(webhook, message)):
            sent_count += 1
            failed_previous = False
        else:
            if failed_previous:
                print(Fore.RED+" << Ping : YOU ARE BEING RATE LIMITED")
                sleep(30)
            else:
                sleep(1)
            failed_previous = True
        attempt_count += 1
except KeyboardInterrupt:
    print(Fore.CYAN + f"Spam stopped. {sent_count} messages send and {attempt_count} attempts were made.")
    pass
