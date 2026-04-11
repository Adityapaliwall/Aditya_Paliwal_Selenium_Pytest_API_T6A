import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {"text": "Explain how AI works in a few words"}
            ]
        }
    ]
}

response = requests.post(URL, headers=headers, json=payload)

print("Status:", response.status_code)

data = response.json()

if "candidates" in data:
    print(data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print(f"Error from API: {data}")