from fastapi import FastAPI, Request
from app.services.whatsapp_service import process_message

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI WhatsApp Bot is running 🚀"}


@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    print("🔥 Webhook HIT")

    form = await request.form()

    incoming_msg = form.get("Body")
    user_id = form.get("From")

    return await process_message(incoming_msg, user_id)