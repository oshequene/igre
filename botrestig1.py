import requests
import telebot,time
from gdolib import *
from telebot import types
url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'



channel = types.InlineKeyboardButton(text='المطور', url = 't.me/exxxix')

head = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=vEG96oJnlEsyUWNS53bHLkVTMFYQKCBV; ig_did=5D80D38A-797B-482D-A407-4B51217E09E7; ig_nrcb=1; mid=ZEqtPgALAAE-IVt6zG-ZazKzI4qN; datr=jrJKZGOaV4gHwa-Znj2QCVyB',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/?next=%2Faccounts%2Flogout%2F',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'viewport-width': '1261',
    'x-asbd-id': '198387',
    'x-csrftoken': 'vEG96oJnlEsyUWNS53bHLkVTMFYQKCBV',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007389883',
    'x-requested-with': 'XMLHttpRequest',
}

token = "6956462730:AAGPjYs3aW4nzqlatNLpwNWhyrA79ZSxZQ0"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bb = types.InlineKeyboardMarkup()
    bb.add(channel)
    bot.reply_to(message,"ارسل ايميلك لا ترسل اليوزر\n مثال :\nexample@gmail.com",reply_markup=bb)

	
@bot.message_handler(content_types=['text'])
def rest(message):
  email = message.text.strip()
  
  data ={
      "user_email": email
  }

  try:
  	req =requests.post(url,headers=head,data = data).json()
  	st = req['status']
  	if st == 'ok':
  		r = req["obfuscated_email"]
  		bot.reply_to(message,f'تم توصيل الريست:\n{r}')
  	else:
  		bot.reply_to(message,"Sorry, we can't send you a link to reset your password. Please contact Instagram for help.")
  except:
  	bot.reply_to(message,'Error')
 

bot.infinity_polling()
