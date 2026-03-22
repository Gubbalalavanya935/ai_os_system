from groq import Groq
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_response_with_history(messages):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant. "
                        "Give clear, direct, and short answers. "
                        "Avoid unnecessary explanations."
                    )
                }
            ] + messages,
            temperature=0.5,
            max_tokens=150   # ⚡ prevents long responses
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("LLM Error:", e)
        return "Sorry, something went wrong."