from fastapi import Request
from fastapi.responses import Response
from twilio.rest import Client

from app.agents.orchestrator import orchestrator
from app.services.db_service import get_or_create_user
from app.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER
)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def split_message(text, limit=1500):
    return [text[i:i + limit] for i in range(0, len(text), limit)]


async def handle_whatsapp(request: Request):
    form = await request.form()

    incoming_msg = form.get("Body")
    user_id = form.get("From")

    print("🔥 Webhook HIT")
    print(f"[USER]: {incoming_msg} from {user_id}")

    # ✅ Ensure WhatsApp format
    if not user_id.startswith("whatsapp:"):
        user_id = f"whatsapp:{user_id}"

    # ✅ Create user in DB
    get_or_create_user(user_id)

    try:
        reply = orchestrator(user_id, incoming_msg)
        print(f"[BOT]: {reply}")

        parts = split_message(reply)

        for part in parts:
            msg = client.messages.create(
                body=part,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=user_id
            )
            print("✅ Sent:", msg.sid)

    except Exception as e:
        print("❌ Error:", e)

    return Response(content="<Response></Response>", media_type="application/xml")