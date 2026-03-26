import streamlit as st
import requests

# 🔗 Backend URL
BACKEND_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI OS Chat", page_icon="🤖")

# 🧠 Session state
if "user" not in st.session_state:
    st.session_state.user = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# 🔐 LOGIN PAGE
# =========================
if not st.session_state.user:
    st.title("🔐 AI OS Login")

    username = st.text_input("Username")

    if st.button("Login"):
        if username.strip():
            st.session_state.user = username
            st.success(f"Welcome {username} 🚀")
            st.rerun()
        else:
            st.warning("Enter username")

# =========================
# 🤖 CHAT PAGE
# =========================
else:
    st.title(f"🤖 AI Chat ({st.session_state.user})")

    # Logout
    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.messages = []
        st.rerun()

    # Show history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.write(user_input)

        # 🤖 Backend call
        try:
            response = requests.post(
                BACKEND_URL,
                json={
                    "message": user_input,
                    "user_id": st.session_state.user
                },
                timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                ai_reply = data.get("response", "No response")
            else:
                ai_reply = f"❌ Backend error: {response.status_code}"

        except Exception as e:
            ai_reply = f"❌ Error: {e}"

        # Save AI reply
        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_reply
        })

        with st.chat_message("assistant"):
            st.write(ai_reply)