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
        bot.send_message(message.chat.id, f"Спасибо за предоставленный номер телефона: {contact.phone_number}")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("Заполнить анкету")
        markup.add(button)
        bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы подать заявку на ремонт", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Вы не являетесь жителем общежития")

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

if name == 'main':
    bot.polling(none_stop=True)