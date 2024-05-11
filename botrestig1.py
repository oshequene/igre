import telebot,time
from gdolib import *
from telebot import types
channel = types.InlineKeyboardButton(text='المطور', url = 't.me/exxxix')

token = "5919735164:AAE4NDe-UgSDdbIOSJ0TbtS13de_OOpZijQ"
bot = telebot.TeleBot(token)

alokt = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bb = types.InlineKeyboardMarkup()
    bb.add(channel)
    bot.reply_to(message,"ارسل ايميلك لا ترسل اليوزر\n مثال :\nexample@gmail.com",reply_markup=bb)




@bot.message_handler(regexp='gmail.com|yahoo.com|hotmail.com')
def verify_phone_number(message):
    global alokt
    current_time = time.time()
    if current_time - alokt < 200:
        remaining_time = round(200 - (current_time - alokt))
        bot.reply_to(message, "حاول مجددا بعد {} ثانية".format(remaining_time))  
    else:
            reset = gdo_drow.reset(message.text)
            bot.reply_to(message, 'تم ارسال')
            alokt = current_time

print('run')
bot.infinity_polling()()
