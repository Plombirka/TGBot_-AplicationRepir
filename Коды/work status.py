import telebot
from telebot import types

bot = telebot.TeleBot('7083063706:AAEj6EKPw2BdCNawjTwpB9gXMoZQHvbjxr8')

requests = {}  # словарь для хранения заявок и их статусов

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте, отправьте заявку для рассмотрения.")

@bot.message_handler(func=lambda message: True)  
def process_request(message):
    if message.chat.id in requests:    # проверка, если заявка уже существует, отправляется сообщение о том, что предыдущая заявка все еще обрабатывается
        bot.send_message(message.chat.id, "Ваша предыдущая заявка все еще обрабатывается.")
        return

    requests[message.chat.id] = {'full_name': message.from_user.full_name, 'accepted': False}

    # обработка заявки 
    if some_condition:
        requests[message.chat.id]['accepted'] = True
        bot.send_message(message.chat.id, f"Заявка принята! Вашу заявку обрабатывает сотрудник: {some_employee_full_name}")
    else:
        reason = "Нехватка людей"
        bot.send_message(message.chat.id, f"Заявка не принята. Причина: {reason}")  # указывается причина, по которой не приняли заявку

    del requests[message.chat.id]  # удаляем заявку из словаря после обработки

bot.polling(none_stop=True)