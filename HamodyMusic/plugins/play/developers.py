import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from HamodyMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from HamodyMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["حمودي","المالك","مطور السورس","السورس"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fe7de7485c993122bc4a.jpg",
        caption=f"""- Name . : ❪[hamody .](https://t.me/MH_BP)❫
- 𝖴𝖾𝗌 : ❪ @MH_BP ❫
 - i𝖽  : ❪ `6463481188` ❫
- Bio    : متسالنيش عن احوالي انا تايه @M_C_II""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "hamody .", url=f"https://t.me/MH_BP"), 
                 ],[
                   InlineKeyboardButton(
                        "𓏺 ََِ𝗦𝗢𝗨𝗥𝗖𝗘 𝗛𝗔𝗠𝗢𝗗𝗬‌↺", url=f"https://t.me/source_hamody"),
                ],

            ]

        ),

    )
