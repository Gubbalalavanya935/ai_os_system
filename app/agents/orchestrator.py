from app.agents.chat_agent import chat_with_ai

def orchestrator(user_id, message):
    print("🧠 Orchestrator deciding...")

    # Simple logic (can upgrade later)
    if "plan" in message.lower() or "steps" in message.lower():
        return "🧠 Planner coming soon..."

    return chat_with_ai(user_id, message)