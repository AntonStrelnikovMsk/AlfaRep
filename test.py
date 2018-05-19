# -*- coding: utf-8 -*-
import telebot

from telebot import apihelper

apihelper.proxy = {'https':'https://167.99.202.168:80'} # пробовал еще {'https':'167.99.202.168:80'}

TOKEN = '527714449:AAFxfmD4xijNTJo9tqEzSCLEKnhxDinvQK4' # вместо xxx мой токен

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	bot.send_message(message.chat.id, 'Вау правда?')

if __name__ == '__main__':
	bot.polling(none_stop=True)