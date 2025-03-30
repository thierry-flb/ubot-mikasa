import os
from PyroUbot import *
import requests

__MODULE__ = "ʙʀᴀᴛ"
__HELP__ =  """🛠 **BANTUAN UNTUK MODULE BRAT TREND 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .brat (ᴛᴇxᴛ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: untuk membuat text seperti tren tete**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .ʙʀᴀᴛᴠɪᴅᴇᴏ (ᴛᴇxᴛ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: untuk membuat text video seperti tren tete**"""

def get_brat_image(text):
    url = "https://api.botcahx.eu.org/api/maker/brat"
    params = {
        "text": text,
        "apikey": "VENOZY"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
@PY.UBOT("brat")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("gunakan perintah .brat <teks> untuk membuat gambar.")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = get_brat_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah....")

def get_brat_video(text):
    url = "https://api.botcahx.eu.org/api/maker/brat-video"
    params = {
        "text": text,
        "apikey": "VENOZY"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None
        
@PY.UBOT("bratvideo")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("gunakan perintah .bratvideo <teks> untuk membuat gambar.")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    mp4_content = get_brat_video(request_text)
    if mp4_content:
        temp_file = "img.mp4"
        with open(temp_file, "wb") as f:
            f.write(mp4_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah....")
