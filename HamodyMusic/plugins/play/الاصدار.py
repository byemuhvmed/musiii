import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from HamodyMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from HamodyMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["الاصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fe7de7485c993122bc4a.jpg",
        caption=f"""**اهلا بك عزيزي {message.from_user.mention} في اصدار سورس حمودي
- اسم السورس : حمودي

- النوع : ميوزك

- اللغه : اللغه العربيه ويدعم الانجليزيه 

- مجال العمل : بوتات تشغيل الموسيقى في الاتصال
- نظام التشغيل : حمودي بوت ميوزك
- الاصدار 2.0.14

- مطور السورس : [ hamody . ](https://t.me/MH_BP)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ََِ𝗦𝗢𝗨𝗥𝗖𝗘 𝗛𝗔𝗠𝗢𝗗𝗬‌↺", url=f"https://t.me/source_hamody"), 
                 ],[
                 InlineKeyboardButton(
                        "", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )

