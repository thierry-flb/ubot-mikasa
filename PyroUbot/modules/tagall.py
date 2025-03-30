import asyncio
import random
from random import shuffle


from PyroUbot import *



__MODULE__ = "ᴛᴀɢᴀʟʟ"
__HELP__ = """🛠 **BANTUAN UNTUK MODULE TAGALL 」**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .tagall**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴛᴀɢ ᴋᴇ sᴇʟᴜʀᴜʜ ᴀɴɢɢᴏᴛᴀ ɢʀᴏᴜᴘ**

〄➠ **ᴘᴇʀɪɴᴛᴀʜ: .batal**
〄➠ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ᴛᴀɢᴀʟʟ**"""



tagallgcid = []

emoji_categories = {
    "smileys": [
        "😀",
        "😃",
        "😄",
        "😁",
        "😆",
        "😅",
        "😂",
        "🤣",
        "😊",
        "😍",
        "🥰",
        "😘",
        "😎",
        "🥳",
        "😇",
        "🙃",
        "😋",
        "😛",
        "🤪",
    ],
    "animals": [
        "🐶",
        "🐱",
        "🐰",
        "🐻",
        "🐼",
        "🦁",
        "🐸",
        "🦊",
        "🦔",
        "🦄",
        "🐢",
        "🐠",
        "🐦",
        "🦜",
        "🦢",
        "🦚",
        "🦓",
        "🐅",
        "🦔",
    ],
    "food": [
        "🍎",
        "🍕",
        "🍔",
        "🍟",
        "🍩",
        "🍦",
        "🍓",
        "🥪",
        "🍣",
        "🍔",
        "🍕",
        "🍝",
        "🍤",
        "🥗",
        "🥐",
        "🍪",
        "🍰",
        "🍫",
        "🥤",
    ],
    "nature": [
        "🌲",
        "🌺",
        "🌞",
        "🌈",
        "🌊",
        "🌍",
        "🍁",
        "🌻",
        "🌸",
        "🌴",
        "🌵",
        "🍃",
        "🍂",
        "🌼",
        "🌱",
        "🌾",
        "🍄",
        "🌿",
        "🌳",
    ],
    "travel": [
        "✈️",
        "🚀",
        "🚲",
        "🚗",
        "⛵",
        "🏔️",
        "🚁",
        "🚂",
        "🏍️",
        "🚢",
        "🚆",
        "🛴",
        "🛸",
        "🛶",
        "🚟",
        "🚈",
        "🛵",
        "🛎️",
        "🚔",
    ],
    "sports": [
        "⚽",
        "🏀",
        "🎾",
        "🏈",
        "🎱",
        "🏓",
        "🥊",
        "⛳",
        "🏋️",
        "🏄",
        "🤸",
        "🏹",
        "🥋",
        "🛹",
        "🥏",
        "🎯",
        "🥇",
        "🏆",
        "🥅",
    ],
    "music": ["🎵", "🎶", "🎤", "🎧", "🎼", "🎸", "🥁", "🎷", "🎺", "🎻", "🪕", "🎹", "🔊"],
    "celebration": ["🎉", "🎊", "🥳", "🎈", "🎁", "🍰", "🧁", "🥂", "🍾", "🎆", "🎇"],
    "work": ["💼", "👔", "👓", "📚", "✏️", "📆", "🖥️", "🖊️", "📂", "📌", "📎"],
    "emotions": ["❤️", "💔", "😢", "😭", "😠", "😡", "😊", "😃", "🙄", "😳", "😇", "😍"],
}


def emoji_random():
    random_category = random.choice(tuple(emoji_categories.keys()))
    return random.choice(emoji_categories[random_category])


@PY.UBOT("tagall")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if message.chat.id in tagallgcid:
        return
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
        f"<a href=tg://user?id={member.user.id}>{emoji_random()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await m.reply_text(
            f"{text}\n\n{' '.join(output)}", quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(2)
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass


@PY.UBOT("batal")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if message.chat.id not in tagallgcid:
        return await message.reply_text(
            "tidak ada <blockquote>🚦perintah tagall yang digunakan"
        )
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text("tagall berhasil dibatalkan")
