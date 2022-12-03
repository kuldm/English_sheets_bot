from __future__ import print_function
from datetime import datetime
import gspread
from googletrans import Translator

translater = Translator()


def word_list():
    # Задём путь к credentials.json
    gc = gspread.service_account(filename='credentials.json')
    # Задаём имя нашей таблицы и имя листа с которого будем получать данные
    worksheet = gc.open("Words").worksheet('WordList')
    # Для получения значений задаём с какой по какую ячейку считывать данные
    values = worksheet.get('A1:B300')
    words_dict = {}  # Словарь в котором ключ это слово на английском(1 сторблец таблицы), а значение это перевод на русский (2 столбец таблицы)
    for i in values:
        words_dict[i[0]] = i[1]

    return words_dict


if __name__ == '__main__':
    word_list()
