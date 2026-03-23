from fastapi import FastAPI, Request
from app.services.whatsapp_service import handle_whatsapp

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI WhatsApp Bot is running 🚀"}


@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    print("🔥 Webhook HIT")
    return await handle_whatsapp(request)