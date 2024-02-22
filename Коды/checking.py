import telebot
from telebot import types

bot = telebot.TeleBot('7083063706:AAEj6EKPw2BdCNawjTwpB9gXMoZQHvbjxr8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Отправить номер телефона', request_contact=True))
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы отправить свой номер телефона.",
                     reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def contact_received(message):
    contact = message.contact
    bot.send_message(message.chat.id, f"Спасибо за предоставленный номер телефона: {contact.phone_number}")

bot.polling(none_stop=True)
