import telebot

bot = telebot.TeleBot('7593971995:AAEDgzOjrOibR2v5PUstM1xiOUFg54taQUc') #TOKEN

@bot.message_handler(commands=['start']) #look funct
def main(message):
    bot.send_message(message.chat.id, 'ку') #SEND MESSAGE

bot.polling(none_stop=True) #START BOT