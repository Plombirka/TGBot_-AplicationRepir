import telebot
from telebot import types
import psycopg2
from psycopg2 import Error
import time
import threading

TOKEN = '7081394328:AAFGSiobnfr9BRe8CoXiiJ7tH_s7W6zquY8'
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

# Обработчик получения контакта
@bot.message_handler(content_types=['contact'])
def contact_received(message):
    global contact
    contact = message.contact
    sql = f"SELECT id FROM work WHERE id = %s"
    cursor.execute(sql, (contact.phone_number,))
    number = cursor.fetchone()
    print(contact.phone_number)
    print(number)
    print(cursor.fetchone())
    if number:
        number = str(number[0])
    if number:
        bot.send_message(message.chat.id, f"Спасибо за предоставленный номер телефона: {contact.phone_number}")
        chat_id=message.chat.id
        print(chat_id)
        cursor.execute(f'UPDATE work SET chatid = %s WHERE id = %s',(chat_id,contact.phone_number))
        conn.commit()
        threading.Thread(target=zayvka(message)).start()
    else:
        bot.send_message(message.chat.id, f"Вы не являетесь сотрудником")

def zayvka(message):
    za = True
    while za == True:
        global Id
        cursor.execute(f"SELECT job_title FROM work WHERE id = {contact.phone_number}")
        job_work = cursor.fetchone()[0]
        cursor.execute(f'SELECT chatid FROM work WHERE id = {contact.phone_number}')
        chat_id = cursor.fetchone()[0]
        sql = f"SELECT id, fio_stud, frame, room, description FROM applications WHERE status = 'В обработке' and job_title = '{job_work}'"
        cursor.execute(sql)
        job = cursor.fetchone()
        if job is not None:
            print(job)
            Id = job[0]
            FIO = job[1]
            korpus = job[2]
            room = job[3]
            description = job[4]
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            item = types.KeyboardButton("Принять")
            markup.add(item)
            item = types.KeyboardButton("Отклонить")
            markup.add(item)
            bot.send_message(chat_id, f"ФИО студента: {FIO}\nКорпус №{korpus}\nКомната №{room}\nОписание работы: {description}",reply_markup=markup)
            za = False
        else:
            time.sleep(7)

@bot.message_handler(func=lambda message: message.text in ["Принять","Отклонить"])
def handle_messages(message):
    global Id,za
    if message.text == "Принять":
        za = True
        bot.send_message(message.chat.id, "Заявка принята!")
        cursor.execute(f"SELECT fio FROM work WHERE id = {contact.phone_number}")
        FIO = cursor.fetchone()[0]
        cursor.execute(f"UPDATE applications SET status = 'В работе', fio_work = '{FIO}' WHERE id = %s",(Id,))
        conn.commit()
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item = types.KeyboardButton("Завершить заявку")
        markup.add(item)
        bot.send_message(message.chat.id, "Нажмите на кнопку если работа была выполнена", reply_markup=markup)

    elif message.text == "Отклонить":
        za = True
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item = types.KeyboardButton("Недостаточно рук")
        markup.add(item)
        item = types.KeyboardButton("Нет подходящих инструментов")
        markup.add(item)
        item = types.KeyboardButton("Другое")
        markup.add(item)
        bot.send_message(message.chat.id, "Выберите причину отклонения:", reply_markup=markup)

@bot.message_handler(func = lambda message:message.text in ["Недостаточно рук","Нет подходящих инструментов", "Другое"])
def handle_message(message):
    if message.text == "Недостаточно рук" or message.text == "Нет подходящих инструментов":
        bot.send_message(message.chat.id, f"Заявка отклонена по причине: {message.text}")
        cursor.execute(f"UPDATE applications SET status = 'Отклонена по причине: {message.text}' WHERE id = %s",(Id,))
        conn.commit()
        threading.Thread(target=zayvka(message)).start()

    elif message.text == "Другое":
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Введите причину отклонения:", reply_markup=hide_markup)
        bot.register_next_step_handler(message, process_other_reason)

@bot.message_handler(func = lambda message:message.text in ["Завершить заявку"])
def handle_message(message):
    if message.text == "Завершить заявку":
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Спасибо за выполнение заявки", reply_markup= hide_markup)
        cursor.execute("UPDATE applications SET status = 'Завершена' WHERE id = %s",(Id,))
        conn.commit()
        threading.Thread(target=zayvka(message)).start()

def process_other_reason(message):
    reason = message.text
    hide_markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, f"Заявка отклонена по причине: {reason}", reply_markup=hide_markup)
    cursor.execute(f"UPDATE applications SET status = 'Отклонена по причине: {reason}' WHERE id = %s",(Id,))
    conn.commit()
    threading.Thread(target=zayvka(message)).start()

if __name__ == "__main__":
    # Запускаем телеграм-бота
    bot.polling(none_stop=True)