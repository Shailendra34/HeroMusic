# ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐ @SHAILENDRA34 | 
# ๐๐๐๐ซ ๐๐๐ซ๐จ ๐ฉ๐ฉ๐ฅ๐ฌ ๐๐ฅ๐ข๐ฌ๐ก ๐๐จ๐ง'๐ญ ๐ซ๐๐ฆ๐จ๐ฏ๐ ๐ญ๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ ๐๐ซ๐จ๐ฆ ๐ก๐๐ซ๐ ๐


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """สแดส {}\n\nแดสsแดสา {} \nแด sษชแดแดสแด , สแดษข าสแดแด แดษดแด าสแดxษชสสแด แดแดsษชแด สแดแด ๐ท\nษชา สแดแด าแดแดษชษดษข แดษดส ษชssแดแด สแดสแดแดแดแด แดแด แดสษชs แดแดsษชแด สแดแด แดสแดษด แดสแดแดsแด แดแดษชษด @{}\nาแดส แดแดสแด สแดสแด สแดแด แดแดษด แดxแดสแดสแดส สแดสแด แดแดษดแด สส แดแดแดแดษชษดษข แดษด /help ๐ฅ"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="๐๐ฉ๐๐๐ญ๐๐ฌ ๐ซ", url=f"https://t.me/HeroOfficialBots"),
                    InlineKeyboardButton(text="๐๐๐ ๐๐ โ", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="๐๐ฐ๐ง๐๐ซ'๐ฑ๐ โญ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="๐๐๐ฏ โจ", url="https://t.me/Shailendra34"),
                ],                
                [                    
                    InlineKeyboardButton(text="๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐", callback_data="help_"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """สแดษช {}\nสแดสแด ษชs แดสแด สแดสแด แดแดษดแด แดสแดแดsแด สแดแดส แดแดsษชสแด แดแดแดษชแดษด ษดแด แดxแดสแดสแดส ษชแด\nาแดส แดษดส แดษชษดแด แดา สแดสแด แดส วซแดแดสส แดแดsแด แดแดษชษด @{} แดษดแด แดsแด สแดแดส วซแดแดสส ๐ซ"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="๐ สแดsษชแด", callback_data="basic_"),
            InlineKeyboardButton(text="๐ แดแดแด?แดษดแดแด", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="๐ แดสแดsแด", callback_data="close_"),
            InlineKeyboardButton(text="โฌ๏ธ สแดแดแด", callback_data="HOME"),
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
    
        HELP_TXT = f"""สแดษช, สแดสแด ษชs แดสแด สแดสแด แดแดษดแด แดสแดแดsแด สแดแดส แดแดsษชสแด แดแดแดษชแดษด ษดแด แดxแดสแดสแดส ษชแด\nาแดส แดษดส แดษชษดแด แดา สแดสแด แดส วซแดแดสส แดแดsแด แดแดษชษด @{SUPPORT_GROUP} แดษดแด แดsแด สแดแดส วซแดแดสส ๐ซ"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="๐ สแดsษชแด", callback_data="basic_"),
                InlineKeyboardButton(text="๐ แดแดแด?แดษดแดแด", callback_data="admin_cmd"),
            ],
            [
                InlineKeyboardButton(text="๐ แดสแดsแด", callback_data="close_"),
                InlineKeyboardButton(text="โฌ๏ธ สแดแดแด", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""สแดส, แดสsแดสา {BOT_NAME} \nแด sษชแดแดสแด , สแดษข าสแดแด แดษดแด าสแดxษชสสแด แดแดsษชแด สแดแด ๐ฅ\nษชา สแดแด าแดแดษชษดษข แดษดส ษชssแดแด สแดสแดแดแดแด แดแด แดสษชs แดแดsษชแด สแดแด แดสแดษด แดสแดแดsแด แดแดษชษด @{SUPPORT_GROUP}\nาแดส แดแดสแด สแดสแด สแดแด แดแดษด แดxแดสแดสแด สแดสแด แดแดษดแด สส แดแดแดแดษชษดษข แดษด /help """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="๐๐ฉ๐๐๐ญ๐๐ฌ ๐ซ", url=f"https://t.me/HeroOfficialBots"),
                    InlineKeyboardButton(text="๐๐๐ ๐๐ โ", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="๐๐ฐ๐ง๐๐ซ'๐ฑ๐ โญ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="๐๐๐ฏ โจ", url="https://t.me/Shailendra34"),
                ],                
                [                    
                    InlineKeyboardButton(text="๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "basic_":
        B_HELP = """
`สแดsษชแด แดแดแดแดแดษดแดs :- `

/play (query, ytlink, audio file) - use this command and enjoy music
/ytp (query) - Use it for better search music!!
/song (query) - Download your favourite songs using this command!
/search (query) - This command will give you youtube search of your query!
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="๐ แดสแดsแด", callback_data="close_"),
                InlineKeyboardButton(text="โฌ๏ธ สแดแดแด", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin_cmd":
        A_HELP = """
`แดแดแดษชษดs แดแดแดแดแดษดแดs :-`

/pause - To pause the song!
/resume - Resume paused song!
/skip - skip to the next song!
/end - End the stream!
/join - To invite assistant in your group!


`sแดแดแด แดแดแดแดแดษดแด :-`

/rmf - To clean Download file from database
/rmw - To clean raw files from database
/clean - To clean files from server
/gcast - To globel casting a msg
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="๐ แดสแดsแด", callback_data="close_"),
                InlineKeyboardButton(text="โฌ๏ธ สแดแดแด", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
