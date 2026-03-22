from fastapi.responses import Response
from app.agents.chat_agent import chat_with_ai
from twilio.rest import Client
from app.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER
)

# Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


# ✅ Split long messages (Twilio limit fix)
def split_message(text, limit=1500):
    return [text[i:i + limit] for i in range(0, len(text), limit)]


async def process_message(incoming_msg, user_id):
    # 🔥 DEBUG
    print("🔥 process_message called")
    print(f"[USER]: {incoming_msg} from {user_id}")

    # ❌ Safety check
    if not incoming_msg or not user_id:
        print("❌ Missing Body or From")
        return Response(
            content='<?xml version="1.0"?><Response></Response>',
            media_type="application/xml"
        )

    # ⚡ Instant reply
    instant_reply = "Processing your request... ⏳"

    try:
        # 🤖 Generate AI response
        reply = chat_with_ai(user_id, incoming_msg)
        print(f"[BOT]: {reply}")

        # ✅ Split long messages
        parts = split_message(reply)

        # ✅ FIX: Ensure WhatsApp format
        if not user_id.startswith("whatsapp:"):
            user_id = f"whatsapp:{user_id}"

        if not TWILIO_WHATSAPP_NUMBER.startswith("whatsapp:"):
            from_number = f"whatsapp:{TWILIO_WHATSAPP_NUMBER}"
        else:
            from_number = TWILIO_WHATSAPP_NUMBER

        # ✅ Send via Twilio
        for part in parts:
            msg = client.messages.create(
                body=part,
                from_=from_number,
                to=user_id
            )
            print("✅ Sent SID:", msg.sid)

    except Exception as e:
        print("❌ Error:", e)

    # ✅ Clean TwiML response
    twiml_response = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Response>'
        f'<Message>{instant_reply}</Message>'
        '</Response>'
    )

    return Response(content=twiml_response, media_type="application/xml")