import telebot

bot = telebot.TeleBot("5919401327:AAHlByvIwXn9EcE9oyWDJhyM_YfVBHB0DQQ")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi!")

bot.polling(none_stop=True)