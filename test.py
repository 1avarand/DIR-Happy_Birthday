import requests
import base64
from datetime import datetime

# Base64 decode the webhook
WEBHOOK_B64 = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM5MTEyMzY4MTg0OTI0NTg0OS81OGlReUFOVkd1WWZWZHlCbXlOUGU3NnlKNENYQUlsdVFzN2pnQ0JyQkFfSUtvVnQyVVByZm5kVXpES3pCLWVRWk5kSA=="
WEBHOOK_URL = base64.b64decode(WEBHOOK_B64).decode("utf-8")

# Avatar and name
AVATAR_URL = "https://cdn.discordapp.com/attachments/1380235317222834268/1391123367255347291/image.png?ex=686ac018&is=68696e98&hm=0561199f4586e0835cce396bbb83a9e000e6e1a789f418528860e7a228b4ac95&"
USERNAME = "Happy Birthday"

#if celebrants:
for name in celebrants:
    data = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "embeds": [
            {
                "title": f"🎉 Happy Birthday, minte! 🎂",
                "description": f"Let's all wish **minte** a wonderful birthday today! 🥳",
                "color": 0xFF69B4
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"Successfully sent birthday wish to {name}.")
    else:
        print(f"Failed to send for {name}: {response.status_code} - {response.text}")