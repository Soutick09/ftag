from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_ID = 28450765
API_HASH = "36f00f11f9d5c65e69b81fd804453a93"
TOKEN = "7935129195:AAFdhMvLXFwqtrxq2h2lXwnKvbCR1YJIBm8"

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
        "Welcome to Tag Remover Bot!\n\nAdd me to your channel with FULL PERMISSIONS.",
        reply_markup=buttons,
    )

# Handle forwarded messages
@app.on_message(filters.private & filters.forwarded)
async def handle_forwarded_message(client, message):
    # Repost the message to the same chat without forward tag
    await message.copy(message.chat.id)
    # Delete the original forwarded message
    await message.delete()

# Handle normal text or media messages
@app.on_message(filters.private & (filters.text | filters.media))
async def handle_regular_message(client, message):
    # Process normal messages (not forwarded)
    await message.copy(message.chat.id)
    await message.delete()

app.run()
