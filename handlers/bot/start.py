# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 | 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """ʜᴇʏ {}\n\nᴍʏsᴇʟғ {} \nᴀ sɪᴍᴘʟᴇ , ʟᴀɢ ғʀᴇᴇ ᴀɴᴅ ғʟᴇxɪʙʟᴇ ᴍᴜsɪᴄ ʙᴏᴛ 🌷\nɪғ ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ᴛʜᴇɴ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ @{}\nғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ʏᴏᴜ ᴄᴀɴ ᴇxᴘʟᴏʀᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴏɴ /help 💥"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬 💫", url=f"https://t.me/Royalkifeelings"),
                    InlineKeyboardButton(text="𝐀𝐝𝐝 𝐌𝐞 ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ⭐", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="𝐃𝐞𝐯 ✨", url="https://t.me/Royal_boy_amit"),
                ],                
                [                    
                    InlineKeyboardButton(text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 📒", callback_data="help_"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """ʜᴏɪ {}\nʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴅᴇsɪʀᴇ ᴏᴘᴛɪᴏɴ ɴᴅ ᴇxᴘʟᴏʀᴇʀ ɪᴛ\nғᴏʀ ᴀɴʏ ᴋɪɴᴅ ᴏғ ʜᴇʟᴘ ᴏʀ ǫᴜᴇʀʏ ᴊᴜsᴛ ᴊᴏɪɴ @{} ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ 💫"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="📒 ʙᴀsɪᴄ", callback_data="basic_"),
            InlineKeyboardButton(text="📒 ᴀᴅᴠᴀɴᴄᴇ", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close_"),
            InlineKeyboardButton(text="⬅️ ʙᴀᴄᴋ", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""ʜᴏɪ, ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴅᴇsɪʀᴇ ᴏᴘᴛɪᴏɴ ɴᴅ ᴇxᴘʟᴏʀᴇʀ ɪᴛ\nғᴏʀ ᴀɴʏ ᴋɪɴᴅ ᴏғ ʜᴇʟᴘ ᴏʀ ǫᴜᴇʀʏ ᴊᴜsᴛ ᴊᴏɪɴ @{SUPPORT_GROUP} ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ 💫"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="📒 ʙᴀsɪᴄ", callback_data="basic_"),
                InlineKeyboardButton(text="📒 ᴀᴅᴠᴀɴᴄᴇ", callback_data="admin_cmd"),
            ],
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ ʙᴀᴄᴋ", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""ʜᴇʏ, ᴍʏsᴇʟғ {BOT_NAME} \nᴀ sɪᴍᴘʟᴇ , ʟᴀɢ ғʀᴇᴇ ᴀɴᴅ ғʟᴇxɪʙʟᴇ ᴍᴜsɪᴄ ʙᴏᴛ 💥\nɪғ ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ᴛʜᴇɴ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ @{SUPPORT_GROUP}\nғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ʏᴏᴜ ᴄᴀɴ ᴇxᴘʟᴏʀᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴏɴ /help """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬 💫", url=f"https://t.me/Royalkifeelings"),
                    InlineKeyboardButton(text="𝐀𝐝𝐝 𝐌𝐞 ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ⭐", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="𝐃𝐞𝐯 ✨", url="https://t.me/Royal_boy_amit"),
                ],                
                [                    
                    InlineKeyboardButton(text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 📒", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "basic_":
        B_HELP = """
`ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs :- `

/play (query, ytlink, audio file) - use this command and enjoy music
/ytp (query) - Use it for better search music!!
/song (query) - Download your favourite songs using this command!
/search (query) - This command will give you youtube search of your query!
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin_cmd":
        A_HELP = """
`ᴀᴅᴍɪɴs ᴄᴏᴍᴍᴀɴᴅs :-`

/pause - To pause the song!
/resume - Resume paused song!
/skip - skip to the next song!
/end - End the stream!
/join - To invite assistant in your group!


`sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅ :-`

/rmf - To clean Download file from database
/rmw - To clean raw files from database
/clean - To clean files from server
/gcast - To globel casting a msg
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
