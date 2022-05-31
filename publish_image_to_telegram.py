import os
import random

import telegram


def get_random_file(folder):
    """
    Возвращает случайный файл из заданной папки.
    Поднимает IndexError, если папка пуста
    """
    return os.path.join(folder, random.choice(os.listdir(folder)))


def publish_image_to_telegram(telegram_token, chat_id, folder):
    photo = get_random_file(folder)
    bot = telegram.Bot(token=telegram_token)
    bot.send_photo(chat_id=chat_id, photo=open(photo, 'rb'))
    os.remove(photo)
