def tool_agent(user_id, message):
    print("🛠 Tool Agent Activated")

    # Simple calculator logic
    try:
        if any(op in message for op in ["+", "-", "*", "/"]):
            result = eval(message)
            return f"🧮 Result: {result}"
    except:
        pass

    # Example API tool (mock)
    if "weather" in message.lower():
        return "🌤 Weather: It's sunny (demo API)"

    return None