from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QTableWidgetItem
import psycopg2

connection = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="91.107.126.60",
    port="5432"
)
connection.autocommit = True
with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio, frame, room FROM stud ORDER BY frame, room;"""
    )
    stud_records = cursor.fetchall()

with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio, job_title, frame FROM work ORDER BY id;"""
    )
    work_records = cursor.fetchall()

with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio_stud, frame, room, fio_work, job_title, description, status FROM applications ORDER BY id;"""
    )
    applications_records = cursor.fetchall()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1014, 510)
        MainWindow.setFixedSize(1014, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_labl = QtWidgets.QLabel(self.centralwidget)
        self.main_labl.setGeometry(QtCore.QRect(330, 0, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_labl.setFont(font)
        self.main_labl.setObjectName("main_labl")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1021, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.stud_page = QtWidgets.QWidget()
        self.stud_page.setObjectName("stud_page")
        self.stud_tableWidget = QtWidgets.QTableWidget(self.stud_page)
        self.stud_tableWidget.setGeometry(QtCore.QRect(0, 10, 1011, 341))
        self.stud_tableWidget.setObjectName("stud_tableWidget")
        self.stud_tableWidget.setColumnCount(4)
        self.stud_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stud_tableWidget.setHorizontalHeaderItem(3, item)
        self.stud_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.stud_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        self.stud_tableWidget.verticalHeader().setVisible(False)

        self.reset_but = QtWidgets.QPushButton(self.centralwidget)
        self.reset_but.setGeometry(QtCore.QRect(950, 15, 50, 50))

        self.stud_save_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.stud_but_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = self.reset_but.font()  # Получаем текущий шрифт
        font.setPointSize(20)  # Устанавливаем размер шрифта (здесь 12)
        self.reset_but.setFont(font)  # Применяем изменения
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.stud_save_add.setFont(font)
        self.stud_save_add.setObjectName("stud_save_add")
        self.stud_but_add.setFont(font)
        self.stud_but_add.setObjectName("stud_but_add")
        self.stud_but_del = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_del.setGeometry(QtCore.QRect(750, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.stud_but_del.setFont(font)
        self.stud_but_del.setObjectName("stud_but_del")
        self.tabWidget.addTab(self.stud_page, "")
        self.work_page = QtWidgets.QWidget()
        self.work_page.setObjectName("work_page")
        self.work_tableWidget = QtWidgets.QTableWidget(self.work_page)
        self.work_tableWidget.setGeometry(QtCore.QRect(0, 10, 1011, 341))
        self.work_tableWidget.setObjectName("work_tableWidget")
        self.work_tableWidget.setColumnCount(4)
        self.work_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.work_tableWidget.setHorizontalHeaderItem(3, item)
        self.work_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.work_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        self.work_tableWidget.verticalHeader().setVisible(False)
        self.work_save_add = QtWidgets.QPushButton(self.work_page)
        self.work_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.work_but_add = QtWidgets.QPushButton(self.work_page)
        self.work_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.work_save_add.setFont(font)
        self.work_save_add.setObjectName("work_save_add")
        self.work_but_add.setFont(font)
        self.work_but_add.setObjectName("work_but_add")
        self.work_but_del = QtWidgets.QPushButton(self.work_page)
        self.work_but_del.setGeometry(QtCore.QRect(750, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.work_but_del.setFont(font)
        self.work_but_del.setObjectName("work_but_del")
        self.tabWidget.addTab(self.work_page, "")
        self.applications_page = QtWidgets.QWidget()
        self.applications_page.setObjectName("applications_page")
        self.applications_tableWidget = QtWidgets.QTableWidget(self.applications_page)
        self.applications_tableWidget.setGeometry(QtCore.QRect(0, 10, 1011, 341))
        self.applications_tableWidget.setObjectName("applications_tableWidget")
        self.applications_tableWidget.setColumnCount(8)
        self.applications_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.applications_tableWidget.setHorizontalHeaderItem(7, item)
        self.applications_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.applications_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) #Растягивание строк
        self.applications_tableWidget.verticalHeader().setVisible(False)
        self.applications_but_add = QtWidgets.QPushButton(self.applications_page)
        self.applications_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applications_but_add.setFont(font)
        self.applications_but_add.setObjectName("applications_but_add")
        self.applications_save_add = QtWidgets.QPushButton(self.applications_page)
        self.applications_save_add.setGeometry(QtCore.QRect(300, 360, 181, 61))
        self.applications_but_del = QtWidgets.QPushButton(self.applications_page)
        self.applications_but_del.setGeometry(QtCore.QRect(550, 360, 181, 61))
        self.reloud_but = QtWidgets.QPushButton(self.applications_page)
        self.reloud_but.setGeometry(QtCore.QRect(800, 360, 70, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applications_save_add.setFont(font)
        self.applications_save_add.setObjectName("applications_save_add")
        self.applications_but_del.setFont(font)
        self.applications_but_del.setObjectName("applications_but_del")
        self.reloud_but.setFont(font)
        self.reloud_but.setObjectName("reloud_but")
        self.tabWidget.addTab(self.applications_page, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        for row_index, record in enumerate(stud_records):
            self.stud_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.stud_tableWidget.setItem(row_index, col_index, item)

        for row_index, record in enumerate(work_records):
            self.work_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.work_tableWidget.setItem(row_index, col_index, item)

        for row_index, record in enumerate(applications_records):
            self.applications_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.applications_tableWidget.setItem(row_index, col_index, item)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панель администратора"))
        self.main_labl.setText(_translate("MainWindow", "Панель администратора"))
        item = self.stud_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.stud_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.stud_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Корпус"))
        item = self.stud_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Комната"))

        self.reset_but.setText(_translate("MainWindow", "🗘"))
        self.reloud_but.setText(_translate("MainWindow", "🗘"))

        self.stud_save_add.setText(_translate("MainWindow", "Сохранить"))
        self.stud_but_add.setText(_translate("MainWindow", "Добавить"))
        self.stud_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stud_page), _translate("MainWindow", "Студенты"))
        item = self.work_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.work_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.work_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.work_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Корпус"))
        self.work_save_add.setText(_translate("MainWindow", "Сохранить"))
        self.work_but_add.setText(_translate("MainWindow", "Добавить"))
        self.work_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_page), _translate("MainWindow", "Работники"))
        item = self.applications_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.applications_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО студента"))
        item = self.applications_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Корпус"))
        item = self.applications_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Комната"))
        item = self.applications_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ФИО работника"))
        item = self.applications_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.applications_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.applications_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Статус"))
        self.applications_save_add.setText(_translate("MainWindow", "Сохранить"))
        self.applications_but_add.setText(_translate("MainWindow", "Добавить"))
        self.applications_but_del.setText(_translate("MainWindow", "Удалить"))
        self.reloud_but.setText(_translate("MainWindow", "🗘"))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.applications_page), _translate("MainWindow", "Заявки"))

    def add_function(self):
        self.stud_but_add.clicked.connect(self.add_record_stud)
        self.stud_but_del.clicked.connect(self.delete_records_stud)
        self.stud_save_add.clicked.connect(self.save_stud)

        self.work_but_add.clicked.connect(self.add_record_work)
        self.work_but_del.clicked.connect(self.delete_records_work)
        self.work_save_add.clicked.connect(self.save_work)

        self.applications_but_add.clicked.connect(self.add_record_applications)
        self.applications_but_del.clicked.connect(self.delete_records_applications)
        self.applications_save_add.clicked.connect(self.save_applications)

        self.reloud_but.clicked.connect(self.reset_table)

        self.reset_but.clicked.connect(self.reset)

    def reset_table(self):
        self.applications_tableWidget.clearContents()
        self.applications_tableWidget.setRowCount(0)

        connection = psycopg2.connect(
            database="exampledb",
            user="docker",
            password="docker",
            host="91.107.126.60",
            port="5432"
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT id, fio_stud, frame, room, fio_work, job_title, description, status FROM applications ORDER BY id;"""
            )
            applications_records2 = cursor.fetchall()

        for row_index, record in enumerate(applications_records2):
            self.applications_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.applications_tableWidget.setItem(row_index, col_index, item)
        connection.close()

    def reset(self):
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)


    def add_record_stud(self):
            row_count = self.stud_tableWidget.rowCount()
            self.stud_tableWidget.insertRow(row_count)

            conn = psycopg2.connect(
                database="exampledb",
                user="docker",
                password="docker",
                host="91.107.126.60",
                port="5432"
            )

            cur = conn.cursor()
            cur.execute("SELECT fio FROM all_stud")
            data = cur.fetchall()

            combo = QComboBox() #ФИО
            combo.addItems([item[0] for item in data])
            self.stud_tableWidget.setCellWidget(row_count, 1, combo)

            # self.stud_but_add.setEnabled(False)

    def delete_records_stud(self):
        try:
            selected_row = self.stud_tableWidget.currentRow()  # Получение индекса выбранной строки
            if selected_row >= 0:
                item = self.stud_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
                id = item.text()  # Получение текста из элемента
                # Удаление записи из базы данных
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM stud WHERE id = %s;", (id,))
                # Удаление строки из таблицы
        except Exception as e:
            pass
        self.stud_tableWidget.removeRow(selected_row)

    def add_record_work(self):
        row_count = self.work_tableWidget.rowCount()
        self.work_tableWidget.insertRow(row_count)


    def delete_records_work(self):
        try:
            selected_row = self.work_tableWidget.currentRow()  # Получение индекса выбранной строки
            if selected_row >= 0:
                item = self.work_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
                id = item.text()  # Получение текста из элемента
                # Удаление записи из базы данных
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM work WHERE id = %s;", (id,))
                # Удаление строки из таблицы
                self.work_tableWidget.removeRow(selected_row)
        except Exception as e:
            pass
        self.work_tableWidget.removeRow(selected_row) 

    def add_record_applications(self):
        row_count = self.applications_tableWidget.rowCount()
        self.applications_tableWidget.insertRow(row_count)

        # Получение значения id из предыдущей записи
        previous_id_item = self.applications_tableWidget.item(row_count - 1, 0)
        previous_id = int(previous_id_item.text()) if previous_id_item is not None else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Автозаполнение поля "id" в таблице
        id_item = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.applications_tableWidget.setItem(row_count, 0, id_item)

        conn = psycopg2.connect(
            database="exampledb",
            user="docker",
            password="docker",
            host="91.107.126.60",
            port="5432"
        )

        cur = conn.cursor()
        cur.execute("SELECT fio FROM stud")
        data = cur.fetchall()


        combo = QComboBox()
        combo.addItems([item[0] for item in data])
        self.applications_tableWidget.setCellWidget(row_count, 1, combo)

        cur = conn.cursor()
        cur.execute("SELECT DISTINCT job_title FROM work")
        data1 = cur.fetchall()

        combo = QComboBox()
        combo.addItems([item[0] for item in data1])
        self.applications_tableWidget.setCellWidget(row_count, 5, combo)

        cur = conn.cursor()
        cur.execute("SELECT fio FROM work")
        data1 = cur.fetchall()

        combo = QComboBox()
        combo.addItems([item[0] for item in data1])
        self.applications_tableWidget.setCellWidget(row_count, 4, combo)

        combo = QComboBox() #Статус
        combo.addItem("В обработке")
        combo.addItem("Завнершенно")
        combo.addItem("Не завнершенно")
        self.applications_tableWidget.setCellWidget(row_count, 7, combo)        

    def delete_records_applications(self):
        try:
            selected_row = self.applications_tableWidget.currentRow()  # Получение индекса выбранной строки
            if selected_row >= 0:
                item = self.applications_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
                id = item.text()  # Получение текста из элемента
                # Удаление записи из базы данных
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM applications WHERE id = %s;", (id,))
                # Удаление строки из таблицы
                self.applications_tableWidget.removeRow(selected_row)
        except Exception as e:
            pass
        self.applications_tableWidget.removeRow(selected_row)

    def save_stud(self):
        connection = psycopg2.connect(
        database="exampledb",
        user="docker",
        password="docker",
        host="91.107.126.60",
        port="5432"
        )
        connection.autocommit = True
        try:
            overcrowded_rooms = set()  # Множество для отслеживания номеров комнат с переполнением

            for row in range(self.stud_tableWidget.rowCount()):
                fio_widget = self.stud_tableWidget.cellWidget(row, 1)

                id_item = self.stud_tableWidget.item(row, 0)

                id_text = id_item.text()

                if id_item is None or id_item.text() == "" :
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле  id не должно быть пустым.")
                    return
                elif len(id_text) != 11:
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле id должно содержать 11 символов.")
                    return
                id = int(id_item.text())

                frame_item = self.stud_tableWidget.item(row, 2)
                if frame_item is None or frame_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле № корпуса не должно быть пустым.")
                    return
                frame = int(frame_item.text())

                room_item = self.stud_tableWidget.item(row, 3)
                if room_item is None or room_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле № комнаты не должно быть пустым.")
                    return
                room = int(room_item.text())

                if frame > 5 or frame <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № корпуса (от 1 до 5).")
                    return

                if room > 300 or room <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № комнаты (от 1 до 300).")
                    return

                # Проверяем, что хотя бы одно из полей не пустое
                if fio_widget is not None:
                    fio = fio_widget.currentText() if fio_widget is not None else ""

                    # Проверяем перенаселение только если номер комнаты еще не был обнаружен переполненным
                    if room not in overcrowded_rooms:
                        with connection.cursor() as cursor:
                            cursor.execute("SELECT COUNT(*) FROM stud WHERE frame = %s AND room = %s", (frame, room))
                            count = cursor.fetchone()[0]

                        if count >= 2:
                            overcrowded_rooms.add(room)  # Добавляем номер комнаты в множество переполненных
                            QMessageBox.warning(MainWindow, "Ошибка", "Перенаселение в корпусе {} комнате {}.".format(frame,room))
                            continue  # Пропускаем сохранение текущей записи и переходим к следующей

                    with connection.cursor() as cursor:
                        cursor.execute("SELECT fio, frame, room FROM stud WHERE id = %s", (id,))
                        original_data = cursor.fetchone()

                    if original_data is not None:
                        original_fio, original_frame, original_room = original_data
                        if fio != original_fio or frame != original_frame or room != original_room:
                            with connection.cursor() as cursor:
                                cursor.execute("UPDATE stud SET fio = %s, frame = %s, room = %s WHERE id = %s",
                                            (fio, frame, room, id))
                            # Обновляем флаг переполнения только в случае, если произошли изменения в записи
                            overcrowded_rooms.discard(room)  # Удаляем комнату из множества переполненных, если она была там
                    else:
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO stud (id, fio, frame, room) VALUES (%s, %s, %s, %s)",
                                        (id, fio, frame, room))

            connection.commit()
            print("Данные сохранены в таблицу Студенты.")
        except Exception as e:
            print("Ошибка при сохранении или редактировании данных:", e)

        try:  # Редактирование
            for row in range(self.stud_tableWidget.rowCount()):
                id = self.stud_tableWidget.item(row, 0).text()
                fio = self.stud_tableWidget.item(row, 1).text()
                frame = int(self.stud_tableWidget.item(row, 2).text())
                room = int(self.stud_tableWidget.item(row, 3).text())

                if frame > 5 or frame <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № корпуса (от 1 до 5).")
                    return

                if room > 300 or room <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № комнаты (от 1 до 300).")
                    return

                # Проверяем, не приводит ли обновление комнаты к ее переполнению
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM stud WHERE frame = %s AND room = %s AND id != %s", (frame, room, id))
                    count = cursor.fetchone()[0]

                if count >= 2:
                    QMessageBox.warning(MainWindow, "Ошибка", "Перенаселение в комнате №{}.".format(room))
                    continue  # Пропускаем обновление текущей записи и переходим к следующей

                # Обновляем запись в базе данных
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE stud SET fio = %s, frame = %s, room = %s WHERE id = %s",
                                (fio, frame, room, id))
            connection.commit()
        except Exception as a:
            print("Данные не изменены")
   
        self.stud_tableWidget.clearContents()
        self.stud_tableWidget.setRowCount(0)

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT id, fio, frame, room FROM stud ORDER BY frame, room;""")
            stud_records = cursor.fetchall()

        for row_index, record in enumerate(stud_records):
            self.stud_tableWidget.insertRow(row_index)
            for col_index, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.stud_tableWidget.setItem(row_index, col_index, item)

    def save_work(self):
        try:
            for row in range(self.work_tableWidget.rowCount()):
                id_item = self.work_tableWidget.item(row, 0)
                if id_item is None or id_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле  id не должно быть пустым.")
                    return
                id = int(id_item.text())

                fio_item = self.work_tableWidget.item(row, 1)
                if fio_item is None or fio_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле ФИО не должно быть пустым.")
                    return
                fio = fio_item.text()

                if fio_item is None or fio_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле ФИО не должно быть пустым.")
                    return


                job_title_item = self.work_tableWidget.item(row, 2)
                if job_title_item is None or job_title_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле Должность не должно быть пустым.")
                    return
                job_title = job_title_item.text()

                if job_title_item is None or job_title_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле Должность не должно быть пустым.")
                    return


                frame_item = self.work_tableWidget.item(row, 3)
                if frame_item is None or frame_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле № корпуса не должно быть пустым.")
                    return
                frame = int(frame_item.text())

                if frame_item is None or frame_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле № корпуса не должно быть пустым.")
                    return

                frame = int(frame_item.text())

                with connection.cursor() as cursor:
                    cursor.execute("SELECT fio, job_title, frame FROM work WHERE id = %s", (id,))
                    original_data = cursor.fetchone()

                if original_data is not None:
                    original_frame = original_data
                    if frame != original_frame:
                        with connection.cursor() as cursor:
                            cursor.execute("UPDATE work SET fio = %s, job_title = %s, frame = %s WHERE id = %s", (fio, job_title, frame, id))
                else:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO work (id, fio, job_title, frame) VALUES (%s, %s, %s, %s)", (id, fio, job_title, frame))

            connection.commit()
            print("Данные сохранены в таблицу Работники.")
        except Exception as e:
            print("Ошибка при сохранении или редактировании данных:", e)

        try:
            for row in range(self.work_tableWidget.rowCount()):
                id = self.work_tableWidget.item(row, 0).text()
                fio = self.work_tableWidget.item(row, 1).text()
                job_title = self.work_tableWidget.item(row, 2).text()
                frame = int(self.work_tableWidget.item(row, 3).text())

                if frame > 5 or frame <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № корпуса (от 1 до 5).")
                    return

                with connection.cursor() as cursor:
                    cursor.execute("SELECT fio, job_title, frame FROM work WHERE id = %s", (id,))
                    
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE work SET fio = %s, job_title = %s, frame = %s WHERE id = %s", (fio, job_title, frame, id))
            connection.commit()
            
        except Exception as a:
            print("Данные не изменены")   


    def save_applications(self):
        try:
            for row in range(self.applications_tableWidget.rowCount()):
                id = self.applications_tableWidget.item(row, 0).text()
                fio_stud_widget = self.applications_tableWidget.cellWidget(row, 1)

                # frame_widget = self.applications_tableWidget.cellWidget(row, 2)
                # room_widget = self.applications_tableWidget.cellWidget(row, 3)

                fio_work_widget = self.applications_tableWidget.cellWidget(row, 4)
                job_title_widget = self.applications_tableWidget.cellWidget(row, 5)
                status_widget = self.applications_tableWidget.cellWidget(row, 7)

                description_item = self.applications_tableWidget.item(row, 6)
                try:
                    description = description_item.text().strip()
                except AttributeError:
                    QMessageBox.warning(MainWindow, "Ошибка", "Не удалось получить описание для заявки.")
                    return

                if not description:
                    QMessageBox.warning(MainWindow, "Ошибка", "Не введено описание для заявки.")
                    return

                frame_item = self.applications_tableWidget.item(row, 2)
                if frame_item is None or frame_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле № корпуса не должно быть пустым.")
                    return

                frame = int(frame_item.text())

                room_item = self.applications_tableWidget.item(row, 3)
                if room_item is None or room_item.text() == "":
                    QMessageBox.warning(MainWindow, "Ошибка", "Поле № комнаты не должно быть пустым.")
                    return

                room = int(room_item.text())


                # Проверяем, что хотя бы одно из полей не пустое
                if fio_stud_widget is not None or fio_work_widget is not None or  job_title_widget is not None or status_widget:
                    fio_stud = fio_stud_widget.currentText() if fio_stud_widget is not None else ""
                    # frame = frame_widget.currentText() if frame_widget is not None else ""
                    # room = room_widget.currentText() if room_widget is not None else ""
                    fio_work = fio_work_widget.currentText() if fio_work_widget is not None else ""
                    job_title = job_title_widget.currentText() if job_title_widget is not None else ""
                    status = status_widget.currentText() if status_widget is not None else ""

                    with connection.cursor() as cursor:
                        cursor.execute("SELECT fio_stud, frame, room, fio_work, job_title, description, status FROM applications WHERE id = %s", (id,))
                        original_data = cursor.fetchone()

                    if original_data is not None:
                        original_fio_stud, original_room, original_fio_work, original_job_title, original_status, original_frame = original_data
                        if fio_stud != original_fio_stud or frame != original_frame or room != original_room or fio_work != original_fio_work or job_title != original_job_title or status != original_status:
                            with connection.cursor() as cursor:
                                cursor.execute("UPDATE applications SET fio_stud = %s, frame = %s, room = %s, fio_work = %s, job_title = %s, description = %s, status = %s, WHERE id = %s", (fio_stud, frame, room, fio_work, job_title, description, status, id))
                    else:
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO applications (id, fio_stud, frame, room, fio_work, job_title, description, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, fio_stud, frame, room, fio_work, job_title, description, status))

            connection.commit()
            print("Данные сохранены в таблицу Заявки.")
        except Exception as e:
            print("Ошибка при сохранении или редактировании данных:", e)

        try:
            for row in range(self.applications_tableWidget.rowCount()):
                id = self.applications_tableWidget.item(row, 0).text()
                fio_stud = self.applications_tableWidget.item(row, 1).text()
                frame = int(self.applications_tableWidget.item(row, 2).text())
                room = int(self.applications_tableWidget.item(row, 3).text())
                fio_work = self.applications_tableWidget.item(row, 4).text()
                job_title = self.applications_tableWidget.item(row, 5).text()
                description = self.applications_tableWidget.item(row, 6).text()
                status = self.applications_tableWidget.item(row, 7).text()

                if frame > 5 or frame <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № корпуса (от 1 до 5).")
                    return

                if room > 300 or room <= 0:
                    QMessageBox.warning(MainWindow, "Ошибка", "Неверный № комнаты (от 1 до 300).")
                    return

                with connection.cursor() as cursor:
                    cursor.execute("SELECT fio_stud, frame, room, fio_work, job_title, description, status FROM applications WHERE id = %s", (id,))
                
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE applications SET fio_stud = %s, frame = %s, room = %s, fio_work = %s,\
                job_title = %s, description = %s, status = %s WHERE id = %s", (fio_stud, frame, room, fio_work, job_title, description, status, id))

            connection.commit()
        except Exception as a:
            print("Данные не изменены") 
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())