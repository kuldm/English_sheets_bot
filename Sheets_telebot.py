import telebot
from telebot import types

from Google_sheets.AdminsAtWork import admin_at_work
from Google_sheets.AdminsNames import admins_name
from Google_sheets.AboutAdmins import about_admins


with open("bots_token.txt", "r", encoding="cp1251") as f:
    bots_token = f.readline()


bot = telebot.TeleBot(bots_token)

