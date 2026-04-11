import streamlit as st
import requests
import os
import html
from dotenv import load_dotenv

# ================== LOAD ENV ==================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# ================== CONFIG ==================
st.set_page_config(page_title="Yin Yang Chat", layout="wide")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

# ================== GEMINI FUNCTION ==================
def get_response(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        res = requests.post(URL, headers=headers, json=payload)

        if res.status_code != 200:
            return f"⚠️ API Error ({res.status_code}): {res.text}"

        data = res.json()
        print(data)  # Debug (optional)

        if "candidates" not in data:
            return f"⚠️ Invalid Response: {data}"

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"⚠️ Connection Error: {str(e)}"


# ================== LOAD CSS ==================
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ================== SESSION STATE ==================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "processing" not in st.session_state:
    st.session_state.processing = False


# ================== LAYOUT ==================
left_yin, right_yang = st.columns(2)

# -------- LEFT (CHAT HISTORY) --------
with left_yin:
    st.markdown('<div class="yin-side">', unsafe_allow_html=True)
    st.title("☯️ Yin")
    st.write("The Dark. The Intuitive.")

    for msg in st.session_state.messages:
        role_class = "user-msg" if msg["role"] == "user" else "bot-msg"

        # ✅ FIX: escape HTML content
        safe_content = html.escape(msg["content"])

        st.markdown(
            f'<div class="{role_class}">{safe_content}</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


# -------- RIGHT (INPUT) --------
with right_yang:
    st.markdown('<div class="yang-side">', unsafe_allow_html=True)
    st.title("Yang")
    st.write("The Light. The Rational.")

    user_input = st.text_input("Speak to the void...", key="input")
    send_btn = st.button("Balance Forces")

    if send_btn and user_input:
        if user_input.lower() == "stop":
            st.warning("Balance closed.")
        else:
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            # 🔥 STATUS MESSAGE
            st.session_state.messages.append({
                "role": "assistant",
                "content": "🔍 Searching...\n🤖 Thinking...\n⚡ Generating response..."
            })

            st.session_state.processing = True
            st.session_state.current_input = user_input
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ================== PROCESS RESPONSE ==================
if st.session_state.get("processing", False):
    response = get_response(st.session_state.current_input)

    # Replace loading message
    st.session_state.messages[-1] = {
        "role": "assistant",
        "content": response
    }

    st.session_state.processing = False
    st.rerun()