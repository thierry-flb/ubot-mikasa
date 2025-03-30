import os
from PyroUbot import *
import requests

__MODULE__ = "ᴄᴀʀʙᴏɴ"
__HELP__ = """🛠 **BANTUAN UNTUK MODULE CARBON 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .carbon (ᴛᴇxᴛ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴀʀʙᴏɴ**"""

def get_carbon_image(text):
    url = "https://itzpire.com/maker/carbon"
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
        
@PY.UBOT("carbon")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("gunakan perintah .carbon <teks> untuk membuat gambar.")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = get_carbon_image(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah....")
