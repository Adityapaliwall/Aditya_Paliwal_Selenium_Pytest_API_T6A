import requests
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
def get_gemini_response(user_text):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_text}
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=payload)
        data = response.json()

        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"Error from API: {data}"
    except Exception as e:
        return f"Connection Error: {str(e)}"


def start_chat():
    print("--- Gemini Chatbot Started (Type 'stop' to exit) ---")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "stop":
            print("Chatbot: Goodbye!")
            break

        if not user_input.strip():
            continue

        response = get_gemini_response(user_input)
        print(f"\nGemini: {response}")


if __name__ == "__main__":
    start_chat()