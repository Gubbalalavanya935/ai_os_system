from fastapi import FastAPI, Form
from fastapi.responses import Response
from app.services.autogen_service import run_autogen

app = FastAPI()


@app.get("/")
def home():
    return {"message": "🚀 WhatsApp AI Bot Running"}


@app.post("/webhook")
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    print("📩 Message:", Body)
    print("👤 From:", From)

    reply = run_autogen(Body, From)

    # ✅ Twilio requires XML (TwiML)
    twiml = f"""
<Response>
    <Message>{reply}</Message>
</Response>
"""

    return Response(content=twiml, media_type="application/xml")