import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from HamodyMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from HamodyMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس ",".","السورس", ".."])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6fe7de7485c993122bc4a.jpg",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [𓏺 ََِ𝗦𝗢𝗨𝗥𝗖𝗘 𝗛𝗔𝗠𝗢𝗗𝗬‌↺](https://t.me/source_hamody)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/MH_BP"), 
                    
                
                    InlineKeyboardButton(
                        " الدعم ", url=f"https://t.me/q_r_II"),
                ],[
                    
                
                    InlineKeyboardButton(
                        " السورس ", url=f"https://t.me/source_hamody"),
                
        ],

            ]

        ),

    )

