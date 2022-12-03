import os
import dotenv

dotenv.load_dotenv('.env')

BOT_API_KEY = os.environ['BOT_API_KEY']  # Ключ Telegram бота

# google_sender_email = os.environ['GMAIL_SENDER_EMAIL']    # Гугл Почта с которой идёт отправка фидбека
# google_password_sender_email = os.environ['GMAIL_PASSWORD_SENDER_EMAIL']    # Пароль доверенного приложения к почте Гугл
# yandex_sender_email = os.environ['YANDEX_SENDER_EMAIL']   # Яндекс Почта с которой идёт отправка фидбека
# yandex_password_sender_email = os.environ['YANDEX_PASSWORD_SENDER_EMAIL']    # Пароль от Яндекс почты
# recipient_email = os.environ['RECIPIENT_EMAIL']    # Почта на которую идёт отправка фидбека
#
# spreadsheet_id = os.environ['WHO_ADMIN_TODAY_SPREADSHEET_ID']   # id google таблицы
#
# yandex_disk_token = os.environ['YANDEX_DISK_TOKEN']    # Token yandex disk

#
# a = {'c': '1', 'n': '2'}
# b = {'g': 'c'}
#
#
#
# if b.get('g') in a:
#     print('да')
# else:
#     print('No')
#
#     dictionary = {'A': 1, 'B': 2, 'C': 3}
#     key = 'B'
#
#     if key in dictionary:
#         print("Key", key, "exists in the dictionary")
#     else:
#         print("Key doesn't exist in the dictionary")
