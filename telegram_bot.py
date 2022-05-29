import telegram

def post_photo(telegram_token, chat_id, file):
    bot = telegram.Bot(token=telegram_token)
    bot.send_photo(chat_id=chat_id, photo=open(file, 'rb'))

telegram_token = "5456681274:AAFa9ITxfuKFtHSt3bUT7ufGoz499YsJUx8"
chat_id = -1001156275886
file = "images/allsky_euve..jpg"

post_photo(telegram_token, chat_id, file)