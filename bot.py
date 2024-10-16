import telebot
from gtts import gTTS
import os

pyTelegramBotAPI
gTTS

worker: python bo.py

# ضع هنا رمز الـ API الخاص بالبوت
BOT_TOKEN = '7613699439:AAHLO_PFkOX84PihE7tEobJjABVQMcNJZ_Q'

# إنشاء كائن البوت
bot = telebot.TeleBot("7613699439:AAHLO_PFkOX84PihE7tEobJjABVQMcNJZ_Q")

# وظيفة لاستقبال الرسائل
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text  # استقبال النص المرسل من المستخدم
    tts = gTTS(text=text, lang='ar')  # تحويل النص إلى صوت باستخدام gTTS
    tts.save("speech.mp3")  # حفظ ملف الصوت
    
    # إرسال ملف الصوت إلى المستخدم
    with open("speech.mp3", "rb") as audio:
        bot.send_audio(message.chat.id, audio)

    # حذف ملف الصوت بعد الإرسال لتوفير المساحة
    os.remove("speech.mp3")

# بدء تشغيل البوت واستقبال الرسائل
bot.polling()
