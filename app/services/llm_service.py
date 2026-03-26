import os
from dotenv import load_dotenv
from groq import Groq

# ✅ Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# 🔴 Safety check
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Check your .env file")

# ✅ Initialize client
client = Groq(api_key=api_key)


def generate_response_with_history(messages):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ Groq Error:", e)
        return "AI error occurred ❌"