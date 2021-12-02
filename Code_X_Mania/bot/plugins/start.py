# (c) Code-X-Mania

from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyshorteners import Shortener

def get_shortlink(url):
   shortlink = False 
   try:
      shortlink = Shortener().dagd.short(url)
   except Exception as err:
       print(err)
       pass
   return shortlink

@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>JOIN UPDATE CHANNEL TO USE ME 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("JOIN 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>𝓢𝓸𝓶𝓮𝓽𝓱𝓲𝓷𝓰 𝔀𝓮𝓷𝓽 𝔀𝓻𝓸𝓷𝓰</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="""
<i>👋 ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡɪᴛʜ ʙᴏᴛʜ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ʟɪɴᴋ ꜱᴜᴘᴘᴏʀᴛ</i>\n
<i>Send a file/video and see magic!<i>\n
<i>Cʟɪᴄᴋ ᴏɴ /help ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><b>It is your responsibility to use wisely I dont take responsibilities of any voilations(of any kind)</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>Dont Spam.</b>""",
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('Owner', url=f"https://t.me/OO7ROBOT"),
                                                                                       InlineKeyboardButton('UPDATES ', url='https://t.me/MyTestBotZ') ] ]  ) )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pʟᴇᴀsᴇ Jᴏɪɴ  Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ**!\n\n**Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh / Try Again",
                                                     url=f"https://t.me/TgInstantLinkBot?start=MyTestBotZ_{usr_cmd}")
                                                     #url=f"https://t.me/{Var.APP_NAME}.herokuapp.com/{usr_cmd}") # Chnage ur app name
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ..",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link2 = Var.URL + 'watch/' + str(get_msg.message_id)
        shortlink = get_shortlink(stream_link2)
        if shortlink:
            stream_link = shortlink
        online_link2 = Var.URL + 'download/' + str(get_msg.message_id)
        shortlinka = get_shortlink(online_link2)
        if shortlinka:
            online_link = shortlinka

        msg_text ="""
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>

<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>

<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>

<b> 🖥WATCH  :</b> <i>{}</i>

<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE</b>

<b>ᴍᴀᴅᴇ ᴡɪᴛʜ❤️ʙʏ @MyTestBotZ</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("sʜᴀʀᴇ & sᴜᴘᴘᴏʀᴛ ᴜs", url=share)],
                                                [InlineKeyboardButton("🖥 STREAM", url=stream_link), #Stream Link
                                                InlineKeyboardButton('Dᴏᴡɴʟᴏᴀᴅ 📥', url=online_link)]]) #Download Link
        )

share = "http://t.me/share/url?url=Hey%20There%E2%9D%A4%EF%B8%8F%2C%0A%20%0A%20I%20Found%20A%20Really%20Awesome%20Bot%20%20For%20Generate%20Direct%20URL%20Link%20of%20any%20Telegram%20Medias.%0A%20Hope%20This%20Bot%20Helps%20You%20Too.%E2%9D%A4%EF%B8%8F%E2%9D%A4%EF%B8%8F%E2%9D%A4%EF%B8%8F%0A%20%0A%20Bot%20Link%20%3A-%20%40TGinstantLinkBot"
@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ FROM USING ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ  Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
   
    await message.reply_text(
       text="Send me any file/media from telegram, I'll provide external direct download link..",
            parse_mode="HTML",
            
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("creator", url="https://t.me/OO7ROBOT")]
            ]
        )
    )

      
      
@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="Sorry DuDe😌, You are Banned to use me🤷. Contact my Master",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⭕ Join Updates Channel⭕", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my Master.",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""➠<b>About Me</b>
        
⭕️<b>My Name : InstantLinkBot</b>

⭕️<b>Creater :</b> @OO7ROBot   

⭕️<b>Channel :</b> @MyTestBotz  

⭕️<b>Server :</b> Railway

⭕️<b>Language :</b> <code>Python3.9.4</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.2.9</a> 

⭕️<b>Build :</b> V2
""",
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⭕Share with Friends ⭕", url="http://t.me/share/url?url=Hey%20There%E2%9D%A4%EF%B8%8F%2C%0A%20%0A%20I%20Found%20A%20Really%20Awesome%20Bot%20%20For%20Generate%20Direct%20URL%20Link%20of%20any%20Telegram%20Medias.%0A%20Hope%20This%20Bot%20Helps%20You%20Too.%E2%9D%A4%EF%B8%8F%E2%9D%A4%EF%B8%8F%E2%9D%A4%EF%B8%8F%0A%20%0A%20Bot%20Link%20%3A-%20%40TGinstantLinkBot"),
                ]
                
            ]
        )
    )      
