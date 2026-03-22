from fastapi import Request
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


async def handle_whatsapp(request: Request):
    form = await request.form()

    incoming_msg = form.get("Body")
    user_id = form.get("From")

    print(f"[USER]: {incoming_msg}")

    # ⚡ Instant reply to avoid timeout
    instant_reply = "Processing your request... ⏳"

    try:
        # 🔥 Generate AI response
        reply = chat_with_ai(user_id, incoming_msg)
        print(f"[BOT]: {reply}")

        # ✅ Split long messages
        parts = split_message(reply)

        # ✅ Send each part via Twilio
        for part in parts:
            msg = client.messages.create(
                body=part,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=user_id
            )
            print("Sent SID:", msg.sid)

    except Exception as e:
        print("Error:", e)

    # ✅ Immediate TwiML response
    twiml_response = f"""
<Response>
    <Message>{instant_reply}</Message>
</Response>
"""

    return Response(content=twiml_response, media_type="application/xml")