from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
    await query.answer("Bot Started")
    await query.edit_message_text(
              f"""**مرحبا عزيزي {message.from_user.mention()}\n
أنا قوي وسهل الاستخدام، يمكنني تشغيل موسيقى عالية الجودة بدون تقطيع في الدردشة الصوتية الجماعية. فقط أضفني الى مجموعتك وقم بإعطائي جميع الصلاحيات ما عدا "التخفي".\n
اعرف المزيد من خلال الازرار الموجوده بالاسفل !!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔍 طريقه تشغيل البوت", callback_data="cb_cmd")
                ],[
                    InlineKeyboardButton("مطور البوت", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("𝐒𝐀𝑳𝐀𝐇 𝐇𝐄𝐌𝐃𝐀𝐍", url=f"https://t.me/Salah_officiall")
                ],[
                    InlineKeyboardButton("𝐉𝐀𝐕𝐀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/JAVA_Supports"),
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀", url=f"https://t.me/JAVA_tlethon")
                ],[
                    InlineKeyboardButton("➕ ضيفني لمجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cb_cmd"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**🤖 أوامر البوت العادية :-

» /play او تشغيل و (اسم الاغنيه)  - لتشغيل الموسيقي
» /skip - تخطي الأغنية
» /end - ايقاف تشغيل الموسيقى
» /pause - أوقف التشغيل مؤقتًا
» /resume - استئناف التشغيل
» /mute - كتم المساعد 
» /search - (إسم الأغنية)



⚙ بعض الأوامر الإضافية :-

» /examine - لاختبار حالة تشغيل البوت
» /start - بدأ البوت
» /id - لجلب ايديك
» /repo - لجلب كود مصدر السورس
» /rmd - حذف كل التنزيلات
» /clean - نظف ملفات التخزين
» /gcast - بث رسالتك


𓆩𝐒𝐎𝐔𝐑𝐂𝐄 𝐉𝐀𝐕𝐀𓆪 ](https://t.me/JAVA_tlethon)**""",
    )

