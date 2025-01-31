
# stickers.py
import random
from config import STICKERS
import telebot

def sticker_handler(message, bot):
    """Обрабатываем стикеры и отправляем их ID"""
    sticker_id = message.sticker.file_id
    print(f"Sticker ID: {sticker_id}")
    bot.reply_to(message, f"ID вашего стикера: {sticker_id}")

def send_random_sticker(message, bot):
    """Отправляем случайный стикер из списка"""
    sticker_id = random.choice(STICKERS)
    bot.send_sticker(message.chat.id, sticker_id)