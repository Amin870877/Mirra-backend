from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# اجازه دسترسی به سایت شما
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

BOT_TOKEN = "8937003688:AAFW1J-bnjoRpi1RlyZ5HDp2MRw76vcHLBU"
CHANNEL_ID = "@dinamit"

@app.get("/check-join")
async def check(user_id: int):
    # درخواست به API تلگرام
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember"
    params = {"chat_id": CHANNEL_ID, "user_id": user_id}
    
    try:
        response = requests.get(url, params=params).json()
        status = response.get("result", {}).get("status")
        
        # اگر عضو باشد یا ادمین باشد
        if status in ["member", "administrator", "creator"]:
            return {"is_member": True}
        return {"is_member": False}
    except:
        return {"is_member": False}
