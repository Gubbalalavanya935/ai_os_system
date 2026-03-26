from app.services.llm_service import generate_response_with_history

# 🧠 In-memory storage
user_memory = {}


def run_autogen(user_message: str, user_id: str):
    try:
        print("🔥 AutoGen START")
        print("User:", user_id)
        print("Message:", user_message)

        # ✅ Initialize memory
        if user_id not in user_memory:
            user_memory[user_id] = [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant. Give clear, detailed, and human-like answers."
                }
            ]

        history = user_memory[user_id]

        # ➕ Add user message
        history.append({"role": "user", "content": user_message})

        # 🤖 Generate response
        response = generate_response_with_history(history)

        # ➕ Save reply
        history.append({"role": "assistant", "content": response})

        # 🔒 Keep last 10 messages
        user_memory[user_id] = history[-10:]

        print("🤖 Reply:", response)

        return response.strip()

    except Exception as e:
        print("❌ AutoGen Error:", e)
        return "Something went wrong ❌"