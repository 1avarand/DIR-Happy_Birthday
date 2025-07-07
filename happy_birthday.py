import requests
import base64
from datetime import datetime

birthdays = [
    ("TEST NAME 0 2025/07/05", "July 5th"),
    ("TEST NAME 1 2025/07/06", "July 6th"),
    ("Rakusane_kup_jim_kalhoty", "July 8th"),
    ("aquadeb1lxv", "July 10th"),
    ("ADIIIIIIIIIIIIIIIIIIIIIIIIII", "April 2"),
    ("Tyler", "November 4"),
    ("goomglayer", "November 25"),
    ("Ariangoodarzi", "April 6"),
    ("faykeee", "July 17th"),
    ("marc7708", "July 7th"),
    ("Gabbah", "February 20th"),
    ("isgoat", "June 30"),
    ("donkpeek", "April 28th"),
    ("roland_pilled_individual", "February 23"),
    ("QUOTE_IF_MEDS_BUTTON", "May 23"),
    ("JoGy2", "April 10"),
    ("Bobbin", "April 13th")
]

# Format today in UTC
today = datetime.utcnow().strftime("%B %-d").replace(" 0", " ")

# Base64 decode the webhook
WEBHOOK_B64 = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM5MTEyMzY4MTg0OTI0NTg0OS81OGlReUFOVkd1WWZWZHlCbXlOUGU3NnlKNENYQUlsdVFzN2pnQ0JyQkFfSUtvVnQyVVByZm5kVXpES3pCLWVRWk5kSA=="
WEBHOOK_URL = base64.b64decode(WEBHOOK_B64).decode("utf-8")

# Avatar and name
AVATAR_URL = "https://cdn.discordapp.com/attachments/1380235317222834268/1391123367255347291/image.png?ex=686ac018&is=68696e98&hm=0561199f4586e0835cce396bbb83a9e000e6e1a789f418528860e7a228b4ac95&"
USERNAME = "Happy Birthday"

# Find celebrants
celebrants = [name for name, bday in birthdays if today.lower() == bday.lower().replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")]

#if celebrants:
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
'''
else:
    # Send a single embed that says it's no one's birthday
    data = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "embeds": [
            {
                "title": "🎂 No Birthdays Today!",
                "description": "Looks like nobody is celebrating today. 🎈",
                "color": 0x7289DA
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Successfully sent 'No birthdays today' message.")
    else:
        print(f"Failed to send: {response.status_code} - {response.text}")
'''