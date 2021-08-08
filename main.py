import os
import telebot

bot = telebot.TeleBot("API Key Here")

@bot.message_hander(commands=["start"])
def send_welcome(message):
|  bot.reply_to(message,"Hello! I Am King Amda Chat Bot")

@bot.message_hander(commands=["help"])
def send_message(message):
    bot.send_message(message, "https://github.com/King-Amda")

bot.polling()
