import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**شكرا لإضافتي في مجموعتك ❤️ \nالآن قم بترقيتي كمسؤول في هذه الدردشة مع الصلاحيات المطلوبة وإلا فلن أتمكن من العمل بشكل صحيح !!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐀𝑳𝐀𝐇 𝐇𝐄𝐌𝐃𝐀𝐍", url=f"https://t.me/Salah_officiall")
                ],[
                    InlineKeyboardButton("𝐉𝐀𝐕𝐀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/JAVA_Supports"),
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url=f"https://t.me/JAVA_tlethon")
                  ],
            ]
        ),
    )
