# ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐๐ @SHAILENDRA34 | 
# ๐๐๐๐ซ ๐๐๐ซ๐จ ๐ฉ๐ฉ๐ฅ๐ฌ ๐๐ฅ๐ข๐ฌ๐ก ๐๐จ๐ง'๐ญ ๐ซ๐๐ฆ๐จ๐ฏ๐ ๐ญ๐ก๐ข๐ฌ ๐ฅ๐ข๐ง๐ ๐๐ซ๐จ๐ฆ ๐ก๐๐ซ๐ ๐


import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors
from helpers.command import commandpro

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command("rmf") & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("`๐๏ธสแดแดแดแด แดแด แดสส าษชสแดs าสแดแด แดแดแดกษดสแดแดแด`")
    else:
        await message.reply_text("`sสส, ษดแดษข ษชs าแดแดษดแด แดแด แดสแดแดษด๐`")

        
@Client.on_message(command("rmw") & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("`แดสแดแดษดษชษดษข sษชสแดษดแด แดส๐๏ธ`")
    else:
        await message.reply_text("`แดสสแดแดแดส แดสแดแดษดแดแด๐โโ๏ธ`")


@Client.on_message(commandpro(["Cl", "/clean", "!clean", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("`โ แดสแดแดษดแดแด`")
    else:
        await message.reply_text("`โ แดสสแดแดแดส แดสแดแดษดแดแด`")
