__MODULE__ = "ʀᴇᴀᴄᴛɪᴏɴ"
__HELP__ = """🛠 **BANTUAN UNTUK MODULE REACTION 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .react (ᴜsᴇʀɴᴀᴍᴇ)**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇᴍʙᴇʀɪᴋᴀɴ ʀᴇᴀᴄᴛɪᴏɴ ᴇᴍᴏᴊɪ**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .stopreact**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ʀᴇᴀᴄᴛɪᴏɴ**"""

from PyroUbot import *
from pyrogram import Client, idle, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatMember
from pyrogram.errors.exceptions import UserNotParticipant

reaction_progress = []

@PY.UBOT("react")
@PY.TOP_CMD
async def react_command(c, m):
    ggl = await EMO.GAGAL(c)
    sks = await EMO.BERHASIL(c)
    prs = await EMO.PROSES(c)
    global reaction_progress
    reaction_progress.append(c.me.id)
    
    if len(m.command) != 3:
        await m.reply(f"<blockquote><b>{ggl}format [emote/id_emoji]</b></blockquote>")
        return

    chat_id = m.command[1]

    rach = await m.reply(f"<b>{prs}proceꜱꜱing..</b>")
    async for message in c.get_chat_history(chat_id):
        if c.me.id not in reaction_progress:
            break
        await asyncio.sleep(0.5)
        chat_id = message.chat.id
        message_id = message.id
        try:
            await c.send_reaction(chat_id=chat_id, message_id=message_id, emoji=m.command[2])
        except Exception:
            pass
    
    await rach.edit(f"<blockquote><b>reaction telah berhaꜱil</b></blockquote>")
    if c.me.id in reaction_progress:
        reaction_progress.remove(c.me.id)


@PY.UBOT("stopreact")
@PY.TOP_CMD
async def stopreact_command(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    global reaction_progress
    if client.me.id in reaction_progress:
        reaction_progress.remove(client.me.id)
        await message.reply(f"<blockquote><b>{sks}berhaꜱil membatalkan reaction</b></blockquote>")
    else:
        await message.reply(f"<blockquote><b>{ggl}tidak ada proses reaction yang sedang berjalan</b></blockquote>")
