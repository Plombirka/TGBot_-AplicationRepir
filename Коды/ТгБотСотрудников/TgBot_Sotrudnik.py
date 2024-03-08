import telebot
from telebot import types

TOKEN = '5775661414:AAGD7PsIHSRdFEqcHRXMszctywjMG9-GgPM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Отправить номер телефона', request_contact=True))
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы отправить свой номер телефона.",
    reply_markup=markup)

# Обработчик получения контакта
@bot.message_handler(content_types=['contact'])
def contact_received(message):
    contact = message.contact
    bot.send_message(message.chat.id, f"Спасибо за предоставленный номер телефона: {contact.phone_number}")
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = types.KeyboardButton("Принять")
    markup.add(item)
    item = types.KeyboardButton("Отклонить")
    markup.add(item)
    bot.send_message(message.chat.id, "Добро пожаловать!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "Принять":
        bot.send_message(message.chat.id, "Заявка принята!")

    elif message.text == "Отклонить":
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item = types.KeyboardButton("Недостаточно рук")
        markup.add(item)
        item = types.KeyboardButton("Нет подходящих инструментов")
        markup.add(item)
        item = types.KeyboardButton("Другое")
        markup.add(item)
        bot.send_message(message.chat.id, "Выберите причину отклонения:", reply_markup=markup)

    elif message.text == "Недостаточно рук" or message.text == "Нет подходящих инструментов":
        bot.send_message(message.chat.id, f"Заявка отклонена по причине: {message.text}")

    elif message.text == "Другое":
        bot.send_message(message.chat.id, "Введите причину отклонения:")
        bot.register_next_step_handler(message, process_other_reason)

def process_other_reason(message):
    reason = message.text
    bot.send_message(message.chat.id, f"Заявка отклонена по причине: {reason}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
