import telebot
from data import *
import command

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi!")

@bot.message_handler(commands=['help'])
def help(message):
    pass



bot.polling(none_stop=True)