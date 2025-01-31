# handlers.py
import random


# Функция для получения user_id
def check_id(message):
    """Получаем user_id из сообщения"""
    user_id = message.from_user.id
    return user_id

# Функция для получения имени пользователя
def name(user_id, bot):
    """Получаем имя пользователя (или username) по user_id"""
    user = bot.get_chat(user_id)  # Получаем объект пользователя по user_id
    return user.first_name if user.first_name else user.username

# Обработчик команды /start
def send_welcome(message, bot):
    """Отправляем приветственное сообщение и получаем имя пользователя"""
    print(f'--- Start handler activated!')
    
    user_id = check_id(message)
    user_name = name(user_id, bot)
    
    print(f'Message from {user_name} (user_id: {user_id})')
    
    bot.reply_to(message, f"Love you, {user_name}!")



# Обработчик для других чатов
def handle_other_message(message, bot):
    """Ответ на сообщения, не из авторизованного чата"""
    bot.reply_to(message, "Я не отвечаю в этом чате.")

def sticker_handler(message, bot):
    """Обрабатываем стикеры и отправляем их ID"""
    sticker_id = message.sticker.file_id
    print(f"Sticker ID: {sticker_id}")
    bot.reply_to(message, f"ID вашего стикера: {sticker_id}")

def handle_message(message, bot):
    
    bot.reply_to(message, "Hi")