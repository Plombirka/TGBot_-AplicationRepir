import telebot
from telebot import types
import psycopg2
from psycopg2 import Error

TOKEN = '6717637833:AAHuVPsSGa5zVbZgYjoH-h3Wgj8hzi_Waf0'
bot = telebot.TeleBot(TOKEN)

try:
    conn = psycopg2.connect(
    database="local",
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
    global contact
    contact = message.contact
    sql = f"SELECT id FROM stud WHERE id = %s"
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
        button = types.KeyboardButton("Создать заявку")
        markup.add(button)
        bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы подать заявку на ремонт", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Вы не являетесь жителем общежития")

@bot.message_handler(func=lambda message:message.text in ["Создать заявку"])
def handle_text(message):
    global job
    if message.text == "Создать заявку":
        sql = f"SELECT DISTINCT job_title FROM work"
        cursor.execute(sql)
        job = cursor.fetchall()
        print(job)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for item in job:
            markup.add(types.KeyboardButton(item[0]))
        bot.send_message(message.chat.id, "Выберете должность нужного работника:", reply_markup= markup)
        bot.register_next_step_handler(message, process_position_step)
    else:
        bot.send_message(message.chat.id, "Используйте кнопки для взаимодействия.")

def process_position_step(message):
    global position
    Dol = True
    for item in job:
        if message.text == str(item[0]):
            position = message.text
            hide_markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, f"Должность: {position}\nВведите описание работы:", reply_markup=hide_markup)
            Dol = False
            bot.register_next_step_handler(message, process_description_step)
    if Dol == True:
        return

def process_description_step(message):
    global id_max
    description = message.text
    bot.send_message(message.chat.id, f"Описание работы: {description}\nСпасибо за создание заявки! Ваша заявка будет рассмотрена в ближайшее время.")
    stud = f"SELECT fio, frame, room FROM stud WHERE id = {contact.phone_number}"
    cursor.execute(stud)
    info_stud = cursor.fetchone()
    id_auto_sql = f"SELECT id FROM applications"
    cursor.execute(id_auto_sql)
    id_auto = cursor.fetchall()
    id_max = 0
    if id_auto is not None:
        for i in range(len(id_auto)):
            id_auto_item = id_auto[i][0]
            if(id_max<int(id_auto_item)):
                id_max = id_auto_item
    id_max += 1
    sql = f"INSERT INTO applications (id, fio_stud, frame, job_title, description, status, room) VALUES ({id_max}, '{info_stud[0]}','{info_stud[1]}','{position}','{description}','В обработке','{info_stud[2]}')"
    cursor.execute(sql)
    conn.commit()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Узнать статус")
    markup.add(button)
    bot.send_message(message.chat.id, "Нажмите на кнопку что бы узнать статус вашей заявки", reply_markup=markup)

@bot.message_handler(func=lambda message:message.text in ["Узнать статус"])
def handle_text(message):
    cursor.execute(f"SELECT status FROM applications WHERE id = {id_max}")
    status = cursor.fetchone()[0]
    if status == "В обработке":
        bot.send_message(message.chat.id,"Ваша заявка ещё не была принята не одинм сотрудником")
    elif status == "В работе":
        cursor.execute(f"SELECT fio_work FROM applications WHERE id = {id_max}")
        bot.send_message(message.chat.id,f"Ваша заявка была принята сотрудником {cursor.fetchone()[0]}")
    elif status == "Завершена":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("Создать заявку")
        markup.add(button)
        bot.send_message(message.chat.id,"Ваша заявка завершена, можете создать ещё одну заявку, для этого нажмите на кнопку", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("Создать заявку")
        markup.add(button)
        bot.send_message(message.chat.id,f"Ваша заявка была {status}",reply_markup=markup)
if name == 'main':
    bot.polling(none_stop=True)