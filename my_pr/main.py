import telebot
import schedule
import time
import random 
import re
from my_pr.config import TOKEN, AUTHORIZED_CHAT_ID
from my_pr.handlers import send_welcome, handle_message, sticker_handler  # Импортируем sticker_handler
from my_pr.stickers import send_random_sticker  # Импортируем функцию для отправки стикеров


# Инициализация бота
bot = telebot.TeleBot(TOKEN)




# Обработчики команд
@bot.message_handler(commands=['start'])
def handle_start(message):
    send_welcome(message, bot)

@bot.message_handler(func=lambda message: re.match(r'.*#сделалдело', message.text))

def handle_random_sticker(message):
    send_random_sticker(message, bot)

@bot.message_handler(commands=['id'])
def handle_id(message):
    handle_message(message, bot)

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_handler(message, bot)  # Используем sticker_handler для обработки стикеров

@bot.message_handler(func=lambda message: message.chat.id != AUTHORIZED_CHAT_ID)
def handle_other(message):
    (message, bot)

# Бесконечный цикл для выполнения задач по расписанию
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Пауза в 1 минуту, чтобы не перегружать процессор

# Запуск бота
bot.polling(none_stop=True, interval=0)