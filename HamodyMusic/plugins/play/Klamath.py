import asyncio
import random
from pyrogram import filters, Client
from pyrogram.types import Message
from HamodyMusic import app
import config



txt = [
    "**- اسرع واحد يقول الكلمة** ~ ( بارده)",
    "**- اسرع واحد يقول الكلمة** ~ ( اجيت)",
    "**- اسرع واحد يقول الكلمة*ذ ~ ( جبان)",
    "**- اسرع واحد يقول الكلمة** ~ ( مافهمت)",
    "**- اسرع واحد يقول الكلمة** ~ ( ميت)",
    "**- اسرع واحد يقول الكلمة** ~ ( وصخ)",  
    "**- اسرع واحد يقول الكلمة** ~ ( جوعان)",
    "**- اسرع واحد يقول الكلمة** ~ ( زين)",
    "**- اسرع واحد يقول الكلمة** ~ ( قوي)",
    "**- اسرع واحد يقول الكلمة** ~ ( بطيء)",
    "**- اسرع واحد يقول الكلمة** ~ ( ذكي)",
    "**- اسرع واحد يقول الكلمة** ~ ( خائف)",
    "**- اسرع واحد يقول الكلمة** ~ ( حزين)",
    "**- اسرع واحد يقول الكلمة** ~ ( مستمتع)",
    "**- اسرع واحد يقول الكلمة** ~ ( فرحان)",
    "**- اسرع واحد يقول الكلمة** ~ ( ذو شخصية قوية)",
    "**- اسرع واحد يقول الكلمة** ~ ( واثق)",
    "**- اسرع واحد يقول الكلمة** ~ ( متوتر)",
    "**- اسرع واحد يقول الكلمة** ~ ( مندهش)",
    "**- اسرع واحد يقول الكلمة** ~ ( فائق الذكاء)",
    "**- اسرع واحد يقول الكلمة** ~ ( ذكي للغاية)",
    "**- اسرع واحد يقول الكلمة** ~ ( متسرع)",
    "**- اسرع واحد يقول الكلمة** ~ ( متفائل)",
    "**- اسرع واحد يقول الكلمة** ~ ( متشائم)",
    "**- اسرع واحد يقول الكلمة** ~ ( متفائل جداً)",
    "**- اسرع واحد يقول الكلمة** ~ ( مكتئب)",
    "**- اسرع واحد يقول الكلمة** ~ ( مبتهج)",
    "**- اسرع واحد يقول الكلمة** ~ ( مغمض العينين)",
    "**- اسرع واحد يقول الكلمة** ~ ( مستنكر)",
    "**- اسرع واحد يقول الكلمة** ~ ( مرتبك)",
    "**- اسرع واحد يقول الكلمة** ~ ( متحمس)",
    "**- اسرع واحد يقول الكلمة** ~ ( متعب)",
    "**- اسرع واحد يقول الكلمة** ~ ( مفاجأ)",
    "**- اسرع واحد يقول الكلمة** ~ ( محبوب)",
    "**- اسرع واحد يقول الكلمة** ~ ( مكره)",
    "**- اسرع واحد يقول الكلمة** ~ ( معجب)",
    "**- اسرع واحد يقول الكلمة** ~ ( متواضع)",
    "**- اسرع واحد يقول الكلمة** ~ ( متكبر)",
    "**- اسرع واحد يقول الكلمة** ~ ( متفائل جداً)",
    "**- اسرع واحد يقول الكلمة** ~ ( محبوب للغاية)",
    "**- اسرع واحد يقول الكلمة** ~ ( معفن)",
    "**- اسرع واحد يقول الكلمة** ~ ( محترم)",
    "**- اسرع واحد يقول الكلمة** ~ ( مشاغب)",
    "**- اسرع واحد يقول الكلمة** ~ ( متسلط)",
    "**- اسرع واحد يقول الكلمة** ~ ( متواضع جداً)",
    "**- اسرع واحد يقول الكلمة** ~ ( متهور)",
    "**- اسرع واحد يقول الكلمة** ~ ( مبتكر)",
    "**- اسرع واحد يقول الكلمة** ~ ( ملهم)",
    "**- اسرع واحد يقول الكلمة** ~ ( مضحك)",
    "**- اسرع واحد يقول الكلمة** ~ ( مكتئب جداً)",
    "**- اسرع واحد يقول الكلمة** ~ ( مهتم)",
    "**- اسرع واحد يقول الكلمة** ~ ( محطم)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحياة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحماس)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالتفاؤل)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالسعادة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحزن)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالرغبة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحب)",

    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحنان)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالكراهية)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالامتنان)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالرضا)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالخيبة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحزن)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالفرح)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالندم)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالنجاح)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالفشل)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالتحدي)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحكمة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالجنون)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالسكون",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالحركة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالفكاهة)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالعقلانية)",
    "**- اسرع واحد يقول الكلمة** ~ ( مليء بالجمال)",
]

correct_answers = [
    "بارده",
    "اجيت",
    "جبان",
    "مافهمت",
    "ميت",
    "وصخ",  
    "جوعان",
    "زين",
    "قوي",
    "بطيء",
    "ذكي",
    "خائف",
    "حزين",
    "مستمتع",
    "فرحان",
    "ذو شخصية قوية",
    "واثق",
    "متوتر",
    "مندهش",
    "فائق الذكاء",
    "ذكي للغاية",
    "متسرع",
    "متفائل",
    "متشائم",
    "متفائل جداً",
    "مكتئب",
    "مبتهج",
    "مغمض العينين",
    "مستنكر",
    "مرتبك",
    "متحمس",
    "متعب",
    "مفاجأ",
    "محبوب",
    "مكره",
    "معجب",
    "متواضع",
    "متكبر",
    "متفائل جداً",
    "محبوب للغاية",
    "معفن",
    "محترم",
    "مشاغب",
    "متسلط",
    "متواضع جداً",
    "متهور",
    "مبتكر",
    "ملهم",
    "مضحك",
    "مكتئب جداً",
    "مهتم",
    "محطم",
    "مليء بالحياة",
    "مليء بالحماس",
    "مليء بالتفاؤل",
    "مليء بالسعادة",
    "مليء بالحزن",
    "مليء بالرغبة",
    "مليء بالحب",

    "مليء بالحنان",
    "مليء بالكراهية",
    "مليء بالامتنان",
    "مليء بالرضا",
    "مليء بالخيبة",
    "مليء بالحزن",
    "مليء بالفرح",
    "مليء بالندم",
    "مليء بالنجاح",
    "مليء بالفشل",
    "مليء بالتحدي",
    "مليء بالحكمة",
    "مليء بالجنون",
    "مليء بالسكون",
    "مليء بالحركة",
    "مليء بالفكاهة",  
    "مليء بالعقلانية",  
    "مليء بالجمال",  
]

current_question_index = 0

@app.on_message(filters.command(["كلمه"], ""))
async def game_handler(client: Client, message: Message):
    global current_question_index

    if current_question_index >= len(txt):
        await message.reply("تم انتهاء الأسئلة.")
        return

    current_question = txt[current_question_index]
    correct_answer = correct_answers[current_question_index]

    if message.text.lower() == correct_answer:
        await message.reply("إجابة صحيحة!")
        current_question_index += 1

        if current_question_index < len(txt):
            await message.reply(f"السؤال الحالي: {txt[current_question_index]}")
        else:
            await message.reply("تم انتهاء الأسئلة. شكرًا للمشاركة.")
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")

# Additional code for starting the game or triggering the first question can be added as needed
