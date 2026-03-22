from app.services.llm_service import generate_response_with_history
from app.utils.memory import save_message, get_history

def chat_with_ai(user_id: str, user_input: str) -> str:
    # Save user message
    save_message(user_id, "user", user_input)

    # Get history
    history = get_history(user_id)

    # Get AI response
    response = generate_response_with_history(history)

    # Save AI response
    save_message(user_id, "assistant", response)

    return response