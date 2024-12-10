from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 28450765
API_HASH = "36f00f11f9d5c65e69b81fd804453a93"
TOKEN = "7935129195:AAF5d1A-qEyk8AUJ6QQimatXRaaliXPcGAU"

app = Client("tagremover" , bot_token = TOKEN , api_id = API_ID , api_hash =API_HASH)

@app.on_message(filters.private & filters.text | filters.media )
async def tag(client, message):
 await message.copy(message.chat.id)
 
app.run()
