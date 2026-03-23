from app.services.llm_service import generate_response_with_history

def planner_agent(user_id, message):
    print("🧠 Planner Agent Activated")

    prompt = f"""
You are a planning assistant.

Break the user's request into clear step-by-step instructions.

User request: {message}

Give steps only.
"""

    response = generate_response_with_history([
        {"role": "user", "content": prompt}
    ])

    return f"🧠 Plan:\n{response}"