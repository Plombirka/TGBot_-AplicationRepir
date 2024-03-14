import telebot
from telebot import types
import psycopg2

TOKEN = '5775661414:AAGD7PsIHSRdFEqcHRXMszctywjMG9-GgPM'
bot = telebot.TeleBot(TOKEN)

try:
    conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwerty",
    host="localhost",
    port="5432"
    )
    cursor = conn.cursor()
    print("Connected to PostgreSQL")
except Error as e:
    print(e)

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
    sql = f"SELECT number FROM test WHERE number = %s"
    cursor.execute(sql, (contact.phone_number,))
    number = cursor.fetchone()
    print(contact.phone_number)
    print(number)
    print(cursor.fetchone())
    if number:
        number = str(number[0])
    if number:
        # Запрос для получения текста приветствия из базы данных
        cursor.execute("SELECT text FROM test WHERE number = %s", (number,))
        welcome_text = cursor.fetchone()[0]

        bot.send_message(message.chat.id, f"Спасибо за предоставленный номер телефона: {contact.phone_number}")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item = types.KeyboardButton("Принять")
        markup.add(item)
        item = types.KeyboardButton("Отклонить")
        markup.add(item)

        # Отправка текста приветствия из базы данных
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Вы не являетесь сотрудником")

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
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите причину отклонения:", reply_markup=hide_markup)
        bot.register_next_step_handler(message, process_other_reason)

def process_other_reason(message):
    reason = message.text
    bot.send_message(message.chat.id, f"Заявка отклонена по причине: {reason}")

if __name__ == "__main__":
    # Запускаем телеграм-бота
    bot.polling(none_stop=True)
