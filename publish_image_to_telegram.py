import os
import random

import telegram

from PIL import Image
from io import BytesIO


def compress_image_if_big(file_path):
    """
    Принимает путь до файла с изображением.
    Сокращает изображение на 10%, пока размер на будет меньше 20 МВ.
    Сохраняет изображение по тому же пути.
    """
    image = Image.open(file_path)
    while len(image.tobytes()) >= 20971520:
        length, width = image.size
        image = image.resize((int(length*0.9), int(width*0.9)))
    image.save(file_path)


def get_random_file(folder):
    """
    Возвращает случайный файл из заданной папки.
    Поднимает IndexError, если папка пуста
    Поднимает FileNotFoundError, если папка не существует
    """
    return os.path.join(folder, random.choice(os.listdir(folder)))


def publish_image_to_telegram(telegram_token, chat_id, folder):
    file_path = get_random_file(folder)
    compress_image_if_big(file_path)
    bot = telegram.Bot(token=telegram_token)
    bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'))
    os.remove(file_path)
