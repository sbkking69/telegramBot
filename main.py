import telebot
import data
import command
from classes import * 

bot = telebot.TeleBot(data.token)

@bot.message_handler(commands=['start'])
def start(message):
    command.DownloadDataBase(dataList=data.BaseDateList,path=data.pathBaseData)

    bot.send_message(message.chat.id, "Hi!")

@bot.message_handler(commands=['help'])
def help(message):
    pass
print('hui')


bot.polling(none_stop=True)