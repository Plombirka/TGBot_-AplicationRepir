import telebot
from telebot import types

TOKEN = '7083063706:AAEj6EKPw2BdCNawjTwpB9gXMoZQHvbjxr8'
bot = telebot.TeleBot(TOKEN)

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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Заполнить анкету")
    markup.add(button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы подать заявку на ремонт", reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "Заполнить анкету":
        bot.send_message(message.chat.id, "Введите должность работника:")
        bot.register_next_step_handler(message, process_position_step)
    else:
        bot.send_message(message.chat.id, "Используйте кнопки для взаимодействия.")

def process_position_step(message):
    position = message.text
    bot.send_message(message.chat.id, f"Должность: {position}\nВведите описание работы:")
    bot.register_next_step_handler(message, process_description_step)

def process_description_step(message):
    description = message.text
    bot.send_message(message.chat.id, f"Описание работы: {description}\nСпасибо за заполнение анкеты! Ваша заявка будет рассмотрена в ближайшее время.")

if __name__ == '__main__':
    bot.polling(none_stop=True)