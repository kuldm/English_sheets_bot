import telebot
from telebot import types

import time

import gtts

from settings import BOT_API_KEY
from GoogleSheets import word_list

import gspread

from googletrans import Translator

translater = Translator()  # Это для переводчика

token = BOT_API_KEY  # Токен Бота

bot = telebot.TeleBot(token)


# Хендлер который через функцию отправляет пользователю сообщение с текстом ввести слово, и переходит к следующей функции get_user_word
@bot.message_handler(commands=['addword'])
def get_message(message):
    msg = bot.send_message(message.from_user.id, 'Введите слово на английском:')
    bot.register_next_step_handler(msg, get_user_word)


# Помещаем в словарь по ключу NewWord сообщение введёное пользователем. А позже передаём значение в переменную message в функции
def get_user_word(message):
    start_time = time.monotonic()  # Начало отсчёта для проверки времени работы программы

    words = {}
    words[
        'NewWord'] = message.text.capitalize()  # Получаем слово введеное пользователем и приводим первую буквук слова к верхнему регистру

    if words.get(
            'NewWord') in word_list():  # Если слово введенное юзером есть в таблице, то бот должен отправить перевод этого слова в чат
        WORDS = words.get("NewWord")
        bot.send_message(message.from_user.id,
                         f'{word_list().get(words.get("NewWord"))}')  # Бот отправляет перевод вытаскивая перевод(значение) по ключу(слову введенному пользоватеелм) из таблицы
        audio = open(f'Content/Audio/{WORDS}.mp3', 'rb')
        bot.send_audio(message.from_user.id, audio)  # Бот отправляет аудио которое уже есть в папке
        # bot.send_message(message.from_user.id, f'Прошло {time.monotonic() - start_time}')
        # print(f'Прошло {time.monotonic() - start_time}')

    else:  # Если слова нет в таблице
        WORDS = words.get("NewWord")
        out = translater.translate(WORDS,
                                   dest="ru").text  # Получаем перевод слова являющимся словом которое ввел пользователь с помощью библиотеки гугл транслейт

        length = len(word_list())  # Чтобы добавлять в следующую пустую ячейку узнаем длину нашего словаря

        table_cell_A = 'A' + str(1 + length)  # Прописываем ячейку А в которую нужно добавлять слово
        table_cell_B = 'B' + str(1 + length)

        gc = gspread.service_account(filename='credentials.json')
        worksheet = gc.open("Words").worksheet('WordList')  # Открываем нашу таблицу
        worksheet.update(table_cell_A, WORDS)  # Записываем слово введённое пользователем в ячейку А
        worksheet.update(table_cell_B, out)  # Записываем перевод слова в ячейку B

        tts = gtts.gTTS(WORDS, lang="en")  # Задаём что озвучить и на какой язык с помощью библиотеки gtts
        tts.save(f'Content/Audio/{WORDS}.mp3')  # Сохраняем аудио с именем самого слова

        bot.send_message(message.from_user.id, out)  # Отправляем пользователю перевод слова

        audio = open(f'Content/Audio/{WORDS}.mp3', 'rb')
        bot.send_audio(message.from_user.id, audio)  # Бот отправляет аудио

        bot.send_message(message.from_user.id, 'Слово добавленно')
        # bot.send_message(message.from_user.id, f'Прошло {time.monotonic() - start_time}')
        # print(f'Прошло {time.monotonic() - start_time}')


bot.polling(none_stop=True)
