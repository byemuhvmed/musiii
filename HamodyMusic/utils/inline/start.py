from pyrogram.types import InlineKeyboardButton

import config
from HamodyMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𓏺 ضيفني ↺", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𓏺 الدعم ↺", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𓏺 ضيفني ↺",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="𓏺 **الاوامر** ↺", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𓏺 👤 مطور البوت ↺", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𓏺 الدعم ↺", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="𓏺 قناة المطور ↺", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="𓏺 قناة السورس ↺", url=f"https://t.me/source_hamody"),
        ],
    ]
    return buttons
