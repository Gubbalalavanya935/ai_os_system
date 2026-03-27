from fastapi import FastAPI, Form
from fastapi.responses import Response
from app.services.autogen_service import run_autogen
import html

app = FastAPI()


@app.get("/")
def home():
    return {"message": "🚀 WhatsApp AI Bot Running"}


# ✅ FINAL Twilio Webhook (FIXED)
@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print("📩 Message:", Body)
    print("👤 From:", From)

    reply = run_autogen(Body, From)

    # ✅ Clean + limit message
    clean_reply = html.escape(reply[:1500])

    # ✅ Proper TwiML response
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{clean_reply}</Message>
</Response>
"""

    print("📤 Sending:", clean_reply)

    return Response(content=twiml, media_type="application/xml")