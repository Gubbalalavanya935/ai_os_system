from fastapi import FastAPI
from pydantic import BaseModel
from app.services.autogen_service import run_autogen

app = FastAPI()


# ✅ Request schema
class ChatRequest(BaseModel):
    message: str
    user_id: str


# ✅ Home route
@app.get("/")
def home():
    return {"message": "🚀 AI OS AutoGen Backend Running"}


# ✅ Chat API
@app.post("/chat")
async def chat(req: ChatRequest):
    print("🔥 API HIT")
    print("User:", req.user_id)
    print("Message:", req.message)

    try:
        reply = run_autogen(req.message)

        print("🤖 Reply:", reply)

        return {"response": reply}

    except Exception as e:
        print("❌ ERROR:", e)
        return {"response": f"❌ Error: {str(e)}"}