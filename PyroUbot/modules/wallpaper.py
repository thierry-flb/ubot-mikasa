from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴡᴀʟʟᴘᴀᴘᴇʀ"
__HELP__ = """🛠 **BANTUAN UNTUK MODULE WALLPAPER 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .wall (ᴏ̨ᴜᴇʀʏ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴡᴀʟʟᴘᴀᴘᴇʀ/ɢᴀᴍʙᴀʀ**

〄➠ **ᴏ̨ᴜᴇʀʏ:**
    ⋄ ᴛᴇᴋɴᴏʟᴏɢɪ,
    ⋄ ᴀᴇsᴛʜᴇᴛɪᴄ,
    ⋄ ᴋᴀᴛᴀᴋᴀᴛᴀ,
    ⋄ ʜᴇᴋᴇʀ,
    ⋄ ᴀɴᴊɪɴɢ,
    ⋄ ʜᴘ,
    ⋄ ɢᴀᴍᴇʀ,
    ⋄ ᴘʀᴏɢᴀᴍɪɴɢ,
    ⋄ ᴄʜᴜᴋʏ,
    ⋄ ᴋᴜᴄɪɴɢ"""

URLS = {
    "teknologi": "https://api.botcahx.eu.org/api/wallpaper/teknologi?apikey=VENOZY",
    "aesthetic": "https://api.botcahx.eu.org/api/wallpaper/aesthetic?apikey=VENOZY",
    "katakata": "https://api.botcahx.eu.org/api/wallpaper/katakata?apikey=VENOZY",
    "heker": "https://api.botcahx.eu.org/api/wallpaper/hacker?apikey=VENOZY",
    "anjing": "https://api.botcahx.eu.org/api/wallpaper/anjing?apikey=VENOZY",
    "hp": "https://api.botcahx.eu.org/api/wallpaper/wallhp?apikey=VENOZY",
    "gamer": "https://api.botcahx.eu.org/api/wallpaper/gaming?apikey=VENOZY",
    "progaming": "https://api.botcahx.eu.org/api/wallpaper/programing?apikey=VENOZY",
    "chuky": "https://api.botcahx.eu.org/api/wallpaper/boneka-chucky?apikey=VENOZY",
    "kucing": "https://api.botcahx.eu.org/api/wallpaper/kucing?apikey=VENOZY",
    }


@PY.UBOT("wall")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar anime Error: {e}")
