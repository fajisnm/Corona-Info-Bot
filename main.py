# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "YouTube-info-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://youtube.api.fayas.me/video/getinfo/?query="

START_TEXT = """
Hello {}, I am a simple corona information of a country telegram bot.

Made by @FayasNoushad
"""

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@FayasNoushad.on_message(filters.private & filters.text)
async def reply_info(bot, update):
    reply_markup = BUTTONS
    await update.reply_text(
        text=covid_info(update.text),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )

def covid_info(title):
    try:
        r = requests.get(API + requote_uri(title.lower()))
        info = r.json()
        title = info['title']
        viewCount= info['text']
        thumbnails= info['url,]
        description= info['description']
        info_id = info['id']
        channel = info['name']
        link = info['link']
        keywords = info['keywords']
        publishDate = info['publishDate']
        uploadDate=  in['uploadDate']     
        covid_info = f"""
--**Covid 19 Information**--

title : `{title}`
viewCount : `{acive}`
thumbnails : `{url}`
description : `{description}`
ID : `{id}`
channel : `{name}`
link : `{link}`
keywords : `{keywords}`
publishDate: `{publishDate}`
uploadDate:'{uploadDate}'

Made by @FayasNoushad
"""
        return covid_info
    except Exception as error:
        return error

FayasNoushad.run()
