# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from bs4 import BeautifulSoup
import requests


bughunter0 = Client(
    "WebScrapperBot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)



@bughunter0.on_message(filters.command(["start"]))
async def start(_, message: Message):
    # Edit Your Start string here
    text = f"Hello {message.from_user.first_name}, I am a web scrapper bot." \
    "\nSend me any link for scrapping."
    await message.reply_text(text=text, disable_web_page_preview=True, quote=True)


@bughunter0.on_message((filters.regex("https") | filters.regex("http") | filters.regex("www")) & filters.private)
async def scrapping(bot, message):
    txt = await message.reply_text("Validating Link", quote=True)
    try:  # Extracting Raw Data From Webpage ( Unstructured format)
        url = str(message.text)
        request = requests.get(url)
        await txt.edit(text=f"Getting Raw Data from {url}", disable_web_page_preview=True)
        file_write = open(f'RawData-{message.chat.username}.txt', 'a+')
        file_write.write(f"{request.content}")  # Writing Raw Content to Txt file
        file_write.close()
        await message.reply_document(f"RawData-{message.chat.username}.txt", caption="©@BugHunterBots", quote=True)
        os.remove(f"RawData-{message.chat.username}.txt")
        await txt.delete()
    except Exception as error:
        print(error)
        await message.reply_text(text=f"{error}", disable_web_page_preview=True, quote=True)
        await txt.delete()
        return
    try:
        txt = await message.reply_text(text=f"Getting HTML code from {url}", disable_web_page_preview=True, quote=True)
        soup = BeautifulSoup(request.content, 'html5lib')  # Extracting Html code in Tree Format
        file_write = open(f'HtmlData-{message.chat.username}.txt', 'a+')
        soup.data = soup.prettify()  # parsing HTML
        file_write.write(f"{soup.data}")  # writing data to txt
        file_write.close()
        await message.reply_document(f"HtmlData-{message.chat.username}.txt", caption="©@BugHunterBots", quote=True)
        os.remove(f"HtmlData-{message.chat.username}.txt")
        await txt.delete()
    except Exception as error:
        await message.reply_text(text=f"{error}", disable_web_page_preview=True, quote=True)
        await txt.delete()
        return

# Use soup.find_all('tag_name') to Extract Specific Tag Details
"""
soup.title
# <title>This is Title</title>

soup.title.name
# u'title'

soup.title.string
# u'This is a string'

soup.title.parent.name
# u'head'
"""

bughunter0.run()
