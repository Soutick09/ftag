from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 28450765
API_HASH = "36f00f11f9d5c65e69b81fd804453a93"
TOKEN = "7935129195:AAE93iKW370tuQwmYzEurq3pqBDVDC06cy4"

app = Client("tagremover", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH)

# Command handler for /start
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    # Create an inline button
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Developer", url="https://t.me/Soutick_09")],
            
        ]
    )
    # Send the start message with the inline button
    await message.reply_text(
        "Welcome to Tag Remover Bot!\n\nAdd me in your channel With FULL PERMISSION.",
        reply_markup=buttons,
    )

# Handle forwarded messages
@app.on_message(filters.private & (filters.text | filters.media))
async def tag(client, message):
    # Repost the message to the same chat without forward tag
    await message.copy(message.chat.id)
    # Delete the original message
    await message.delete()

app.run()
