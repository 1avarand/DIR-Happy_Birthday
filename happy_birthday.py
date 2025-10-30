import os
import requests
import base64
from datetime import datetime, timezone

# 🎂 Birthdays stored in MM-DD format
birthdays = [
    ("Rakusane_kup_jim_kalhoty", "07-08"),
    ("aquadeb1lxv", "07-10"),
    ("ADIIIIIIIIIIIIIIIIIIIIIIIIII", "04-02"),
    ("Tyler", "11-04"),
    ("goomglayer", "11-25"),
    ("Ariangoodarzi", "04-06"),
    ("faykeee", "07-17"),
    ("marc7708", "07-07"),
    ("Gabbah", "02-20"),
    ("isgoat", "06-30"),
    ("donkpeek", "04-28"),
    ("roland_pilled_individual", "02-23"),
    ("QUOTE_IF_MEDS_BUTTON", "05-23"),
    ("JoGy2", "04-10"),
    ("Bobbin", "04-13"),
    ("Facts_Giver", "02-03"),
    ("godsuke", "06-12"),
    ("Gaspy", "10-01"),
    ("minte", "08-17"),
    ("moonEEK!", "12-24"),
    ("sexasuke", "10-31"),
    ("deko_1_LanDaLan_final_zywoo_0", "04-03"),
    ("PaNini", "12-17"),
    ("yesi", "04-24"),
    ("FQ_Tommy", "03-01"),
    ("SMALL_NOT_BIG_CLAN", "10-31"),
    ("StefanFlashdeck", "07-07"),
    ("Elextures", "12-18"),
    ("DLDDY", "01-25"),
    ("Vsiion", "03-04"),
    ("novvythebottomfragger", "11-06")
]

def parse_birthday(bday_str: str):
    """Turn 'MM-DD' into (month, day)."""
    month, day = map(int, bday_str.split("-"))
    return month, day

# Today in UTC
today = datetime.now(timezone.utc)
today_tuple = (today.month, today.day)

# Webhook setup
WEBHOOK_URL = os.environ['URL']
USERNAME = "Happy Birthday"
AVATAR_URL = "https://cdn.discordapp.com/attachments/1380235317222834268/1391123367255347291/image.png?ex=68b3eb58&is=68b299d8&hm=45f704355193928d6f7274a73b89446cec7551cf54eab55c257c26d2b61a2109"

# Find celebrants
celebrants = [name for name, bday in birthdays if parse_birthday(bday) == today_tuple]

for name in celebrants:
    data = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "embeds": [
            {
                "title": f"🎉 Happy Birthday, {name}! 🎂",
                "description": f"Let's all wish **{name}** a wonderful birthday today! 🥳",
                "color": 0xFF69B4
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"✅ Successfully sent birthday wish to {name}.")
    else:
        print(f"❌ Failed to send for {name}: {response.status_code} - {response.text}")
