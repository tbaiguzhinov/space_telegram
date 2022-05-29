import telegram

bot = telegram.Bot(token="5456681274:AAFa9ITxfuKFtHSt3bUT7ufGoz499YsJUx8")

my_text = "Че-то намутил, да-да-да"

chat_id = -1001156275886

bot.send_message(chat_id=chat_id, text=my_text)