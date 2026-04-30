from pyrogram import Client, filters
from config import *
from pytgcalls import PyTgCalls

bot = Client(
    "UltimateMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

user = Client(
    "Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

call_py = PyTgCalls(user)

# START COMMAND
@bot.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "🔥 Ultimate Music Bot Active!\nOwner Control Enabled."
    )

# OWNER ONLY COMMAND
@bot.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart(_, message):
    await message.reply_text("♻️ Restarting Bot...")
    import os, sys
    os.execv(sys.executable, ['python'] + sys.argv)

# PLAY COMMAND (DEMO)
@bot.on_message(filters.command("play"))
async def play(_, message):
    await message.reply_text("🎵 Playing Music... (Demo Mode)")

bot.start()
user.start()
call_py.start()

print("🔥 Ultimate Music Bot Started Successfully!")

import idle
idle()
