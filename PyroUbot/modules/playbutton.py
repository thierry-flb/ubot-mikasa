import os
from PyroUbot import *
import requests

__MODULE__ = "ᴘʟᴀʏʙᴜᴛᴛᴏɴ"
__HELP__ = """🛠 **BANTUAN UNTUK MODULE PLAYBUTTON 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .ytsilverplaybutton (ᴛᴇxᴛ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sɪʟᴠᴇʀ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ʏᴏᴜᴛᴜʙᴇ**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .ytgoldplaybutton (ᴛᴇxᴛ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢᴏʟᴅ ᴘʟᴀʏʙᴜᴛᴛᴏɴ ʏᴏᴜᴛᴜʙᴇ**"""

def tweet(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtsilverbutton"
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
def tweets(text):
    url = "https://api.botcahx.eu.org/api/ephoto/twtgoldbutton"
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
def fb(text):
    url = "https://api.botcahx.eu.org/api/ephoto/fbsilverbutton"
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
        
def fbs(text):
    url = "https://api.botcahx.eu.org/api/ephoto/fbgoldbutton"
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
        
def robott(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytsilverbutton"
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
        
def robottt(text):
    url = "https://api.botcahx.eu.org/api/ephoto/igsilverbutton"
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
def robotttg(text):
    url = "https://api.botcahx.eu.org/api/ephoto/iggoldbutton"
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
def horor(text):
    url = "https://api.botcahx.eu.org/api/ephoto/ytgoldbutton"
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

# YOYTUBE        
@PY.UBOT("ytgoldplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .ytgoldplaybutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = horor(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
                              
@PY.UBOT("ytsilverplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .ytsilverplaybutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = robott(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
  
# INSTAGRAM                                
@PY.UBOT("iggoldplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .iggoldplaybutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = robotttg(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")
                                  
@PY.UBOT("igsilverplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .igsilverplaybutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = robottt(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")

# FACEBOOK                                   
@PY.UBOT("fbsilverplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .fbsilverplaybutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = fb(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")

@PY.UBOT("fbgoldplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .fbgoldplaybutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = fbs(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")

# TWITTER
@PY.UBOT("twtsilverplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .twtsilverbutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = tweet(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")

@PY.UBOT("twtgoldplaybutton")
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text("contoh : .twtgoldbutton peno")
        return

    request_text = args[1]
    await message.reply_text("sedang memproses, mohon tunggu...")

    image_content = tweets(request_text)
    if image_content:
        temp_file = "img.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)

        await message.reply_photo(photo=temp_file)
        
        os.remove(temp_file)
    else:
        await message.reply_text("apikey sedang bermasalah")



# CONTACT TELEGRAM @pakveno
# CREDITS NAME VENOOFFICIAL
# CHANNEL TESTIMONI @XXVNBHONC                                                                                                                              