import requests
import base64
from datetime import datetime, timezone

birthdays = [
    ("Rakusane_kup_jim_kalhoty", "July 8"),
    ("aquadeb1lxv", "July 10"),
    ("ADIIIIIIIIIIIIIIIIIIIIIIIIII", "April 2"),
    ("Tyler", "November 4"),
    ("goomglayer", "November 25"),
    ("Ariangoodarzi", "April 6"),
    ("faykeee", "July 17"),
    ("marc7708", "July 7"),
    ("Gabbah", "February 20"),
    ("isgoat", "June 30"),
    ("donkpeek", "April 28"),
    ("roland_pilled_individual", "February 23"),
    ("QUOTE_IF_MEDS_BUTTON", "May 23"),
    ("JoGy2", "April 10"),
    ("Bobbin", "April 13"),
    ("Facts_Giver", "February 3"),
    ("godsuke", "June 12"),
    ("Gaspy", "October 1"),
    ("minte", "August 17")
]

def parse_birthday(bday_str: str):
    """Turn 'July 08' or 'July 8th' into (7, 8)."""
    clean = (
        bday_str.lower()
        .replace("st", "")
        .replace("nd", "")
        .replace("rd", "")
        .replace("th", "")
    ).strip()
    dt = datetime.strptime(clean, "%B %d")
    return dt.month, dt.day

# Today in UTC
today = datetime.now(timezone.utc)
today_tuple = (today.month, today.day)

# Webhook setup
WEBHOOK_B64 = "..."  # your base64 string here
WEBHOOK_URL = base64.b64decode(WEBHOOK_B64).decode("utf-8")
USERNAME = "Happy Birthday"
AVATAR_URL = "https://..."

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
        print(f"Successfully sent birthday wish to {name}.")
    else:
        print(f"Failed to send for {name}: {response.status_code} - {response.text}")
