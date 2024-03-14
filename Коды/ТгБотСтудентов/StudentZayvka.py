import telebot
from telebot import types

TOKEN = '5775661414:AAGD7PsIHSRdFEqcHRXMszctywjMG9-GgPM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Заполнить анкету")
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать.", reply_markup=markup)

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
    bot.send_message(message.chat.id, f"Описание работы: {description}\nСпасибо за заполнение анкеты!")

if __name__ == '__main__':
    bot.polling(none_stop=True)
