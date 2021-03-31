import telebot
import random

API_TOKEN = 'сюда токен'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет, братик')

@bot.message_handler(commands=['monika'])
def start(message):
    bot.reply_to(message, 'https://wallpaperengine.info/wp-content/uploads/2017/10/previewfile_1180201570.jpg')

bot.polling()
