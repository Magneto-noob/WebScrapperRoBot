# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from bs4 import BeautifulSoup
import requests
import time

bughunter0 = Client(
    "WebScrapperBot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)



@bughunter0.on_message(filters.command(["start"]))
async def start(_, message: Message):
    # Edit Your Start string here
    text = f" 👋 Hᴇʟʟᴏ {message.from_user.first_name}, \n\n I ᴀᴍ ᴀ ᴡᴇʙ sᴄʀᴀᴘᴘᴇʀ ʙᴏᴛ.\n Sᴇɴᴅ ᴍᴇ ᴀɴʏ ʟɪɴᴋ ғᴏʀ sᴄʀᴀᴘᴘɪɴɢ. \n\n Cʀᴇᴀᴛᴇᴅ ᴡɪᴛʜ ❤️"
    await message.reply_text(text=text, disable_web_page_preview=True, quote=True)


@bughunter0.on_message((filters.regex("https") | filters.regex("http") | filters.regex("www")) & filters.private)
async def scrapping(bot, message):
   # txt = await message.reply_text(text=f"`Trying to web scrap .........`", disable_web_page_preview=True, quote=True)
    try:  # Extracting Raw Data From Webpage ( Unstructured format)
        url = str(message.text)
        request = requests.get(url)
      # time.sleep(5)
      #  await txt.edit(text=f"Getting Raw Data from {url}", disable_web_page_preview=True)
      #  file_write = open(f'RawData-{message.chat.use.txt', 'a+')
      #  file_write.write(f"{request.content}")  # Writing Raw Content to Txt file
      #  file_write.close()
      #  await message.reply_document(f"RawData-{message.chat.username}.txt", caption="©@BugHunterBots", quote=True)
      #  os.remove(f"RawData-{message.chat.username}.txt")
      #  await txt.delete()
      #      except Exception as error:
      #  print(error)
      #  await message.reply_text(text=f"{error}", disable_web_page_preview=True, quote=True)
      # await txt.delete()
      # return
   # try:
       # txt = await message.reply_text(text=f"Generating HTML Code From {url}", disable_web_page_preview=True, quote=True)
        soup = BeautifulSoup(request.text, 'html.parser')# Extracting Html code in Tree Format
        for title in soup.find_all('title'): 
            titles = title.get_text()
        for link in soup.find_all('source'):
            links = link.get('src')
      # file_write = open(f'{titles}.txt', 'a+')
      # soup.data = soup.prettify()  # parsing HTML
      # file_write.write(f"Title of Video : {titles}\n\nURL of the Video is : {links}")  # writing data to txt
      # file_write.close()
      #  caption = f"`Title :- {titles}`\n\n**Video URL :-** {links}"
      # time.sleep(3)
        await message.reply_text(text=f"`Title :- {titles}`\n\n**Video URL :-** {links}", quote=True)
      # os.remove(f"{titles}.txt")
      #  await txt.delete()
   # except Exception as error:
        await message.reply_text(text=f"{error}", disable_web_page_preview=True, quote=True)
       # await txt.delete()
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
