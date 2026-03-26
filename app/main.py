from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from app.services.autogen_service import run_autogen

app = FastAPI()


@app.get("/")
def home():
    return {"message": "🚀 WhatsApp AI Bot (Groq) Running"}


# ✅ Twilio Webhook
@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print("📩 Message:", Body)
    print("👤 From:", From)

    reply = run_autogen(Body, From)

    return PlainTextResponse(reply)