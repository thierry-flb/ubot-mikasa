import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from pyrogram.errors.exceptions import *
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate

from PyroUbot import *

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ"
__HELP__ =  """**「 BANTUAN UNTUK MODULE BROADCAST 」**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .gikes (ᴛʏᴘᴇ)(ʙᴀʟᴀs/ᴛᴇxᴛ)**
𖠇➛ **ᴛʏᴘᴇ: ᴀʟʟ , ᴜsᴇʀs , ɢʀᴏᴜᴘ**
 **⋄ ᴜsᴇʀs, ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴘʀɪʙᴀᴅɪ**
 **⋄ ɢʀᴏᴜᴘ, ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ɢʀᴏᴜᴘ**
 **⋄ ᴀʟʟ, ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ɢʀᴏᴜᴘ/ᴜsᴇʀ sᴇᴄᴀʀᴀ ʙᴇʀsᴀᴍᴀᴀɴ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .stopg**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴇɴᴛɪᴋᴀɴ ᴘʀᴏsᴇs ɢɪᴋᴇs ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀʟᴀɴɢsᴜɴɢ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .bcfd ᴏʀ .cfd (ᴛʏᴘᴇ)(ʙᴀʟᴀs/ᴛᴇxᴛ)**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sɪᴀʀᴀɴ sᴇᴄᴀʀᴀ ғᴏʀᴡᴀʀᴅ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .send**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ᴜsᴇʀ/ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**

𖠇➛ **ᴘᴇʀɪɴᴛᴀʜ: .autobc (ǫᴜᴇʀʏ)**
𖠇➛ **ǫᴜᴇʀʏ: |on/off |text |delay |remove |limit**
𖠇➛ **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sɪᴀʀᴀɴ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs**

 **⋄ ᴛᴜᴛᴏʀɪᴀʟ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ .bcfd or .cfd:** <a href='https://t.me/tutorbywann/5'>ᴘᴇɴᴄᴇᴛ ᴅɪ sɪɴɪ</a>
 **⋄ ᴛᴜᴛᴏʀɪᴀʟ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ .autobc:** <a href='https://t.me/tutorbywann/6'>ᴘᴇɴᴄᴇᴛ ᴅɪ sɪɴɪ</a>"""

async def limit_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"{prs}processing . . .")
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1) 
    if status and hasattr(status, "text"):
        pjg = len(status.text)
        print(pjg)
        if pjg <= 100:
            if client.me.is_premium:
                text = f"""
᪤➟• {pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ
᪤➟• {tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ
᪤➟• {yubot} ᴜʙᴏᴛ : {bot.me.mention}
"""
            else:
                text = f"""
᪤➟• sᴛᴀᴛᴜs ᴀᴋᴜɴ : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʏᴀ
᪤➟• ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴅɪʙᴀᴛᴀsɪ
᪤➟• ᴜʙᴏᴛ : {bot.me.mention}
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            if client.me.is_premium:
                text = f"""
᪤➟• {pong} sᴛᴀᴛᴜs ᴀᴋᴜɴ ᴘʀᴇᴍɪᴜᴍ : ᴛʀᴜᴇ
᪤➟• {tion} ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ
᪤➟• {yubot} ᴜʙᴏᴛ : {bot.me.mention}
"""
            else:
                text = f"""
᪤➟• sᴛᴀᴛᴜs ᴀᴋᴜɴ : ʙᴇʟɪ ᴘʀᴇᴍ ᴅᴜʟᴜ ʏᴀ
᪤➟• ʟɪᴍɪᴛ ᴄʜᴇᴄᴋ : ᴀᴋᴜɴ ᴀɴᴅᴀ ʙᴇʀᴍᴀsᴀʟᴀʜ
᪤➟• ᴜʙᴏᴛ : {bot.me.mention}
"""
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    else:
        print("status tidak valid atau status.text tidak ada")

gcast_progress = []

@PY.UBOT("bc|gikes")
@PY.TOP_CMD
async def gcast_handler(client, message):
    global gcast_progress
    gcast_progress.append(client.me.id)
    
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    ktrng = await EMO.BL_KETERANGAN(client)    
    _msg = f"<b>{prs}.stop ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ...</b>"
    gcs = await message.reply(_msg)    
    command, text = extract_type_and_msg(message)

    if command not in ["group", "users", "all"] or not text:
        gcast_progress.remove(client.me.id)
        return await gcs.edit(f"{message.text.split()[0]}<b>[ᴛʏᴘᴇ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ]</b> {ggl}")
    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    done = 0
    failed = 0
    for chat_id in chats:
        if client.me.id not in gcast_progress:
            await gcs.edit(f"ᴘʀᴏsᴇs ɢᴄᴀsᴛ ʙᴇʀʜᴀsɪʟ ᴅɪ ʙᴀᴛᴀʟᴋᴀɴ !</b> {sks}")
            return
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await text.copy(chat_id)
            else:
                await client.send_message(chat_id, text)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                if message.reply_to_message:
                    await text.copy(chat_id)
                else:
                    await client.send_message(chat_id, text)
                done += 1
            except (Exception, ChannelPrivate):
                failed += 1
        except (Exception, ChannelPrivate):
            failed += 1

    gcast_progress.remove(client.me.id)
    await gcs.delete()
    _gcs = f"""
<blockquote>᪤➟• {bcs} ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏɴᴇ ʙᴀʏ ɢᴜᴡᴀʜ<\blockquote>
<blockquote>᪤➟• {sks} ʙᴇʀʜᴀsɪʟ : {done} ᴄʜᴀᴛ<\blockquote>
<blockquote>᪤➟• {ggl} ɢᴀɢᴀʟ : {failed} ᴄʜᴀᴛ<\blockquote>
<blockquote>᪤➟• {ktrng} ᴛʏᴘᴇ : {command}<\blockquote>"""

    return await message.reply(_gcs)

@PY.UBOT("stopg")
@PY.TOP_CMD
async def stopg_handler(client, message):
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    global gcast_progress
    if client.me.id in gcast_progress:
        gcast_progress.remove(client.me.id)
        return await message.reply(f"ɢᴄᴀsᴛ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴄᴀɴᴄᴇʟ</b> {sks}")
    else:
        return await message.reply(f"{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ɢᴄᴀsᴛ !!!")

@PY.UBOT("bcfd|cfd")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    
    _msg = f"{prs}ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ..."
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)
    
    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"{ggl}{message.text.split()[0]} type [reply]")

    if not message.reply_to_message:
        return await gcs.edit(f"{ggl}{message.text.split()[0]} type [reply]")

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    _gcs = f"""
<blockquote>᪤➟• {bcs} ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏɴᴇ ʙᴀʏ ɢᴜᴡᴀʜ</blockquote>
<blockquote>᪤➟• {brhsl} ʙᴇʀʜᴀsɪʟ {done} ɢʀᴏᴜᴘ</blockquote>
<blockquote>᪤➟• {ggl} ɢᴀɢᴀʟ {failed} ɢʀᴏᴜᴘ</blockquote>"""
    return await message.reply(_gcs)
#tes


@PY.BOT("broadcast")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("sabar venn lagi proses...\n\nmohon bersabar untuk menunggu proses broadcast sampai selesai", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("mohon balaꜱ atau ketik ꜱeꜱuatu...")
        
    susers = await get_list_from_vars(client.me.id, "SAVED_USERS")
    done = 0
    for chat_id in susers:
        try:
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"pesan broadcast berhasil terkirim ke {done} user\n\n")

@PY.UBOT("addbl")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ..."

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id in blacklist:
            txt = f"""
᪤➟• {grp} ɢʀᴏᴜᴘ: {message.chat.title}
᪤➟• {ktrn} ᴅᴀʜ ᴍᴀsᴜᴋ ᴅɪ ʟɪsᴛ"""
        else:
            await add_to_vars(client.me.id, "BL_ID", chat_id)
            txt = f"""
᪤➟• {grp} ɢʀᴏᴜᴘ: {message.chat.title}\n᪤➟• {ktrn} ᴅᴏɴᴇ ᴀᴅᴅʙʟ ʙᴀʏ ɢᴜᴡᴀʜ"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("unbl")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrn = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ..."

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id not in blacklist:
            response = f"""
᪤➟• {grp} ɢʀᴏᴜᴘ: {message.chat.title}
᪤➟• {ktrn} ɢᴀᴀᴅᴀ ᴅɪ ʟɪsᴛ ᴋᴏɴᴛᴏʟ"""
        else:
            await remove_from_vars(client.me.id, "BL_ID", chat_id)
            response = f"""
᪤➟• {grp} ɢʀᴏᴜᴘ: {message.chat.title}
᪤➟• {ktrn} ᴅᴏɴᴇ ᴅᴇʟᴇᴛᴇ ʙᴀʏ ɢᴜᴡᴀʜ"""

        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("listbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"{prs}ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ..."
    mzg = await message.reply(_msg)

    blacklist = await get_list_from_vars(client.me.id, "BL_ID")
    total_blacklist = len(blacklist)

    list = f"{brhsl} daftar blackliꜱt\n"

    for chat_id in blacklist:
        try:
            chat = await client.get_chat(chat_id)
            list += f" ├ {chat.title} | {chat.id}\n"
        except:
            list += f" ├ {chat_id}\n"

    list += f"᪤➟• {ktrng} total blackliꜱt {total_blacklist}"
    return await mzg.edit(list)


@PY.UBOT("rallbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"{prs}ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ..."

    msg = await message.reply(_msg)
    blacklists = await get_list_from_vars(client.me.id, "BL_ID")

    if not blacklists:
        return await msg.edit(f"{ggl}blackliꜱt broadcaꜱt anda koꜱong")

    for chat_id in blacklists:
        await remove_from_vars(client.me.id, "BL_ID", chat_id)

    await msg.edit(f"{brhsl}ꜱemua blackliꜱt broadcaꜱt berhaꜱil di hapuꜱ")


@PY.UBOT("send")
@PY.TOP_CMD
async def _(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("🤓 ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ ᴀɴᴊ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            if "_" in chat_id:
                msg_id, to_chat = chat_id.split("_")
                return await client.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


@PY.INLINE("^get_send")
async def _(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
        )


AG = []
LT = []


@PY.UBOT("autobc")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    bcs = await EMO.BROADCAST(client)
    mng = await EMO.MENUNGGU(client)
    ggl = await EMO.GAGAL(client)   
    msg = await message.reply(f"{prs}ᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ...")
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit(
                f"{ggl}harap ꜱetting text terlebih dahulu"
            )

        if client.me.id not in AG:
            await msg.edit(f"{brhsl}auto gcaꜱt di aktifkan")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_list_from_vars(client.me.id, "BL_ID")
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                    ):
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} ")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} ")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(f"""
᪤➟• {bcs} ᴀᴜᴛᴏɢᴄᴀsᴛ ᴅᴏɴᴇ ʙᴀʏ ɢᴜᴡᴀʜ
᪤➟• {done} ᴀʟᴀᴍᴀᴋ ᴅᴏɴɢɴᴇ
᪤➟• {brhsl} ʙᴇʀʜᴀsɪʟ {group} ɢʀᴏᴜᴘ
᪤➟• {mng} sᴀʙᴀʀ ᴄᴀᴋ {delay} ᴍɪɴᴜᴛᴇs
""",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit(f"{brhsl}auto gcast dinonaktifkan")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit(
                f"{ggl}{message.text.split()[0]} text - [value]"
            )
        await add_auto_text(client, value)
        return await msg.edit(f"{brhsl}berhasil di simpan")

    elif type == "delay":
        if not int(value):
            return await msg.edit(
                f"{ggl}{message.text.split()[0]} delay - [value]"
            )
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"{brhsl}barhasil ke setting {value} menit"
        )

    elif type == "remove":
        if not value:
            return await msg.edit(
                f"{ggl}{message.text.split()[0]} remove - [value]"
            )
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit(f"{brhsl}semua text berhasil dihapus")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"{brhsl}text ke {value+1} berhasil dihapus"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit(f"{ggl}auto gcast text kosong")
        txt = "daftar auto gcast text\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}> {x}\n\n"
        txt += f"\nuntuk menghapus text:\n{message.text.split()[0]} remove [angka/all]"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit(f"{brhsl}auto cek limit dinonaktifkan")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit(f"{brhsl}auto cek limit started")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
             return await msg.edit(f"{ggl}{message.text.split()[0]} limit - [value]")

    else:
        return await msg.edit(f"{ggl}{message.text.split()[0]} [query] - [value]")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)

@PY.BOT("bcubot")
@PY.ADMIN
async def broadcast_bot(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>", quote=True)
    done = 0
    if not message.reply_to_message:
        return await msg.edit("<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴘᴇsᴀɴ</b>")
    for x in ubot._ubot:
        try:
            await x.unblock_user(bot.me.username)
            await message.reply_to_message.forward(x.me.id)
            done += 1
        except Exception:
            pass
    return await msg.edit(f"ᴅᴏɴᴇ ʙᴀʏ ɢᴜᴡᴀʜ, ᴍᴇɴɢɪʀɪᴍ ᴋᴇ {done} ᴜʙᴏᴛ")
    
