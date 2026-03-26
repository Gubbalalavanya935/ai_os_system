from app.services.llm_service import generate_response_with_history


def run_autogen(user_message: str):
    try:
        print("🔥 AutoGen START")
        print("User Message:", user_message)

        # 🧠 Step 1: Reasoning
        reasoning_prompt = f"""
Think step-by-step and understand the question clearly.

Question: {user_message}
"""

        reasoning = generate_response_with_history([
            {"role": "user", "content": reasoning_prompt}
        ])

        print("🧠 Reasoning:", reasoning)

        # 🤖 Step 2: Final Answer
        final_prompt = f"""
Based on this reasoning, give a clear final answer:

{reasoning}

Answer:
"""

        final_answer = generate_response_with_history([
            {"role": "user", "content": final_prompt}
        ])

        print("✅ Final Answer:", final_answer)

        return final_answer

    except Exception as e:
        print("❌ AutoGen Error:", e)
        return f"❌ Error: {str(e)}"