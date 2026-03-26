from app.services.llm_service import generate_response_with_history


def run_autogen(user_message: str):
    try:
        print("🧠 AutoGen thinking...")

        # 🧠 Step 1: Planning (AutoGen-style reasoning)
        planning_prompt = f"""
You are an intelligent AI agent.

Step 1: Understand the user question
Step 2: Think step-by-step
Step 3: Give a clear and helpful answer

User Question: {user_message}
"""

        plan_response = generate_response_with_history([
            {"role": "user", "content": planning_prompt}
        ])

        print("📋 Plan created")

        # 🤖 Step 2: Final Answer Generation
        final_prompt = f"""
Use the reasoning below to answer clearly:

{plan_response}

Final Answer:
"""

        final_response = generate_response_with_history([
            {"role": "user", "content": final_prompt}
        ])

        print("✅ Final response ready")

        return final_response

    except Exception as e:
        print("❌ AutoGen Error:", e)
        return f"❌ AutoGen Error: {str(e)}"