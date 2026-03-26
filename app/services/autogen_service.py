from app.services.llm_service import generate_response_with_history


def run_autogen(user_message: str):
    try:
        print("🔥 AutoGen START")
        print("User Message:", user_message)

        # 🧠 Step 1: Reasoning (hidden thinking)
        reasoning_prompt = f"""
You are an intelligent AI assistant.

Analyze the question step by step and understand what the user is asking.

Question: {user_message}

Give your reasoning clearly.
"""

        reasoning = generate_response_with_history([
            {"role": "user", "content": reasoning_prompt}
        ])

        print("🧠 Reasoning:", reasoning)

        # 🤖 Step 2: Final Answer (FIXED PROMPT)
        final_prompt = f"""
You are a helpful AI assistant.

Using the reasoning below, provide a complete, clear, and detailed answer to the user's question.

DO NOT answer with "True" or "False".
DO NOT give short answers.
Give a proper explanation.

User Question: {user_message}

Reasoning:
{reasoning}

Final Answer:
"""

        final_answer = generate_response_with_history([
            {"role": "user", "content": final_prompt}
        ])

        print("✅ Final Answer:", final_answer)

        return final_answer.strip()

    except Exception as e:
        print("❌ AutoGen Error:", e)
        return f"❌ Error: {str(e)}"