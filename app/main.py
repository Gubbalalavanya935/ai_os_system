from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from app.services.autogen_service import run_autogen

app = FastAPI()


@app.get("/")
def home():
    return {"message": "🚀 AI OS AutoGen Backend Running"}


# ✅ Twilio WhatsApp Webhook
@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print("📩 Message:", Body)
    print("👤 From:", From)

    try:
        reply = run_autogen(Body)
        print("🤖 Reply:", reply)

        # Twilio expects plain text or TwiML
        return PlainTextResponse(reply)

    except Exception as e:
        print("❌ ERROR:", e)
        return PlainTextResponse("Something went wrong ❌")