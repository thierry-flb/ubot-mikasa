import random
from pyrogram.enums import MessagesFilter
from PyroUbot import *

__MODULE__ = "ᴀsᴜᴘᴀɴ2"
__HELP__ =  """🛠 **BANTUAN UNTUK MODULE ASUPAN 2 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .bokep**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴀsᴜᴘᴀɴ ʙᴏᴋᴇᴘ**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .random**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴀsᴜᴘᴀɴ ʙᴏᴋᴇᴘ ʀᴀɴᴅᴏᴍ**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .vvip**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ʙᴏᴋᴇᴘ ᴠᴠɪᴘ**"""


@PY.UBOT("bokep")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@vvideo_viral", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("random")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupan18tocrot", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
        
@PY.UBOT("vvip")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"{prs}jangan ngocok mulu dek....")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@asupan18tocrot", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
      