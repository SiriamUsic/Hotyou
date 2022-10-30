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


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
     await message.reply_photo(
        photo=f"https://telegra.ph/file/9cbae99908382932e51f0.png",
        caption=f"""**•══•| [ 𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon) |•══• 
        
✨ مرحبا عزيزي صـلاح - ᥉ᥲ️ᥣᥲ️ꫝ { مشغول },.↻!

💭 انا بوت استطيع تشغيل الموسيقي والفديو في محادثتك الصوتية

•══•| 𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon)|•══•**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔍 طريقه تشغيل البوت", callback_data="cb_cmd")
                ],[
                    InlineKeyboardButton("👤 مطور البوت", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀 ", url=f"https://t.me/JAVA_tlethon")
                ],[
                    InlineKeyboardButton("𝐉𝐀𝐕𝐀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/JAVA_Supports"),
                    InlineKeyboardButton("𝐒𝐀𝑳𝐀𝐇 𝐇𝐄𝐌𝐃𝐀𝐍", url=f"https://t.me/Salah_officiall")
                ],[
                    InlineKeyboardButton("✚ ضيفني لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
            ]
        ),
    )


@Client.on_message(command(["examine", f"examine@{BOT_USERNAME}", "فحص"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("جاري فحص البوت...")
    delta_ping = time() - start
    await m_reply.edit_text("**× انا اعمل بالفعل ×**\n\n@JAVA_Supports 📡")


@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("`انقر فوق الزر الموضح أدناه للحصول على شفرة مصدر سورس البوت`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ 𝐒𝐨𝐮𝐫𝐜𝐞 ", url=f"https://t.m/JAVA_Supports")
                ]
            ]
        ),
    )
