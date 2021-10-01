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

API = "https://fajisytdetilsv1.herokuapp.com/api?link=message"

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
        text=youtube_info(update.text),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )

def youtube_info(bot,message):
    try:
        r = requests.get(API + requote_uri(update.text.lower()))
        info = r.json()
        title = info['title']
        views = info['views']
        likes = info['likes']
        channel_name = info['channel_name']
        subscriber = info['subscriber']
        category= info['category']
        dislikes = info['dislikes']
        publishdate = info['publishdate'] 
        youtube_info = f"""
--**YouTube Video Details**--

title : `{title}`
views : `{views}`
likes : `{likes}`
channel_name : `{channel_name}`
subscriber : `{subscriber}`
category : `{category}`
publishdate: `{publishdate}`

Made by @mhdfajis
"""
        return youtube_info
    except Exception as error:
        return error

FayasNoushad.run()
