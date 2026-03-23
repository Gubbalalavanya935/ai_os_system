from app.agents.chat_agent import chat_with_ai
from app.agents.planner_agent import planner_agent
from app.agents.tool_agent import tool_agent

def orchestrator(user_id, message):
    print("🧠 Orchestrator deciding...")

    msg = message.lower()

    # 🧠 Planner trigger
    if "plan" in msg or "steps" in msg:
        return planner_agent(user_id, message)

    # 🛠 Tool trigger
    tool_result = tool_agent(user_id, message)
    if tool_result:
        return tool_result

    # 🤖 Default chat
    return chat_with_ai(user_id, message)