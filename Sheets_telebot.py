import telebot
from telebot import types


with open("bots_token.txt", "r", encoding="cp1251") as f:
    bots_token = f.readline()


bot = telebot.TeleBot(bots_token)