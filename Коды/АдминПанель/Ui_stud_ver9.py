from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QTableWidgetItem
import psycopg2


connection = psycopg2.connect(
    host = "127.0.0.1",
    user = "postgres",
    password = "xkleeps123",
    database = "postgres"
)
connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT version();"
    )
    print(f"Версия сервера: {cursor.fetchone()}")
with connection.cursor() as cursor:
    cursor.execute(
        """SELECT id, fio, frame, room FROM stud ORDER BY id;"""
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
        MainWindow.resize(1014, 510)
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
        self.stud_save_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.stud_but_add = QtWidgets.QPushButton(self.stud_page)
        self.stud_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
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
        self.applications_but_add = QtWidgets.QPushButton(self.applications_page)
        self.applications_but_add.setGeometry(QtCore.QRect(70, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applications_but_add.setFont(font)
        self.applications_but_add.setObjectName("applications_but_add")
        self.applications_save_add = QtWidgets.QPushButton(self.applications_page)
        self.applications_save_add.setGeometry(QtCore.QRect(400, 360, 181, 61))
        self.applications_but_del = QtWidgets.QPushButton(self.applications_page)
        self.applications_but_del.setGeometry(QtCore.QRect(750, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.applications_save_add.setFont(font)
        self.applications_save_add.setObjectName("applications_save_add")
        self.applications_but_del.setFont(font)
        self.applications_but_del.setObjectName("applications_but_del")
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
        item.setText(_translate("MainWindow", "id"))
        item = self.stud_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.stud_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Корпус"))
        item = self.stud_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Комната"))
        self.stud_save_add.setText(_translate("MainWindow", "Сохранить"))
        self.stud_but_add.setText(_translate("MainWindow", "Добавить"))
        self.stud_but_del.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stud_page), _translate("MainWindow", "Студенты"))
        item = self.work_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
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


    def add_record_stud(self):
            row_count = self.stud_tableWidget.rowCount()
            self.stud_tableWidget.insertRow(row_count)

            conn = psycopg2.connect(
                    host = "127.0.0.1",
                    user = "postgres",
                    password = "xkleeps123",
                    database = "postgres"
            )

            cur = conn.cursor()
            cur.execute("SELECT fio FROM all_stud")
            data = cur.fetchall()

            combo = QComboBox()
            combo.addItems([item[0] for item in data])
            self.stud_tableWidget.setCellWidget(row_count, 1, combo)

            combo = QComboBox() #Корпуса
            for i in range(1, 6):
                combo.addItem(f"{i}")
            self.stud_tableWidget.setCellWidget(row_count, 2, combo)

            combo = QComboBox() #Комнаты
            for i in range(1, 301):
                combo.addItem(f"{i}")
            self.stud_tableWidget.setCellWidget(row_count, 3, combo)

    def delete_records_stud(self):
        selected_row = self.stud_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.stud_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM stud WHERE id = %s;", (id,))
            # Удаление строки из таблицы
            self.stud_tableWidget.removeRow(selected_row)


    def add_record_work(self):
        row_count = self.work_tableWidget.rowCount()
        self.work_tableWidget.insertRow(row_count)

        # Получение значения id из предыдущей записи
        previous_id_item = self.work_tableWidget.item(row_count - 1, 0)
        previous_id = int(previous_id_item.text()) if previous_id_item is not None else 0

        # Автогенерированный id для новой записи
        autogenerated_id = previous_id + 1

        # Автозаполнение поля "id" в таблице
        id_item = QtWidgets.QTableWidgetItem(str(autogenerated_id))
        self.work_tableWidget.setItem(row_count, 0, id_item)

        # combo = QComboBox() #ФИО
        # for i in range(1, 4):
        #     combo.addItem(f"ФИО {i}")
        # self.work_tableWidget.setCellWidget(row_count, 1, combo)

        # combo = QComboBox() #Должность
        # combo.addItem("Сантехник")
        # combo.addItem("Электрик")
        # combo.addItem("Завхоз")
        # self.work_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Комнаты
        for i in range(1, 6):
            combo.addItem(f"{i}")
        self.work_tableWidget.setCellWidget(row_count, 3, combo)

    def delete_records_work(self):
        selected_row = self.work_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.work_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM work WHERE id = %s;", (id,))
            # Удаление строки из таблицы
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
                host = "127.0.0.1",
                user = "postgres",
                password = "xkleeps123",
                database = "postgres"
        )

        cur = conn.cursor()
        cur.execute("SELECT fio FROM stud")
        data = cur.fetchall()


        combo = QComboBox()
        combo.addItems([item[0] for item in data])
        self.applications_tableWidget.setCellWidget(row_count, 1, combo)

        combo = QComboBox() #Корпус
        for i in range(1, 6):
            combo.addItem(f"{i}")
        self.applications_tableWidget.setCellWidget(row_count, 2, combo)

        combo = QComboBox() #Корпус
        for i in range(1, 301):
            combo.addItem(f"{i}")
        self.applications_tableWidget.setCellWidget(row_count, 3, combo)

        # combo = QComboBox() #Должность
        # combo.addItem("Сантехник")
        # combo.addItem("Электрик")
        # combo.addItem("Завхоз")

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
        selected_row = self.applications_tableWidget.currentRow()  # Получение индекса выбранной строки
        if selected_row >= 0:
            item = self.applications_tableWidget.item(selected_row, 0)  # Получение элемента из столбца с именем
            id = item.text()  # Получение текста из элемента
            # Удаление записи из базы данных
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM applications WHERE id = %s;", (id,))
            # Удаление строки из таблицы
            self.applications_tableWidget.removeRow(selected_row)


    def save_stud(self):
        try:
            for row in range(self.stud_tableWidget.rowCount()):
                id = self.stud_tableWidget.item(row, 0).text()
                fio_widget = self.stud_tableWidget.cellWidget(row, 1)
                frame_widget = self.stud_tableWidget.cellWidget(row, 2)
                room_widget = self.stud_tableWidget.cellWidget(row, 3)

                # Проверяем, что хотя бы одно из полей не пустое
                if fio_widget is not None or frame_widget is not None or room_widget is not None:
                    fio = fio_widget.currentText() if fio_widget is not None else ""
                    frame = frame_widget.currentText() if frame_widget is not None else ""
                    room = room_widget.currentText() if room_widget is not None else ""

                    with connection.cursor() as cursor:
                        cursor.execute("SELECT fio, frame, room FROM stud WHERE id = %s", (id,))
                        original_data = cursor.fetchone()

                    if original_data is not None:
                        original_fio, original_frame, original_room = original_data
                        if fio != original_fio or frame != original_frame or room != original_room:
                            with connection.cursor() as cursor:
                                cursor.execute("UPDATE stud SET fio = %s, frame = %s, room = %s WHERE id = %s", (fio, frame, room, id))
                    else:
                        with connection.cursor() as cursor:
                            cursor.execute("INSERT INTO stud (id, fio, frame, room) VALUES (%s, %s, %s, %s)", (id, fio, frame, room))

            connection.commit()
            print("Данные сохранены в таблицу Студенты.")
        except Exception as e:
            print("Ошибка при сохранении или редактировании данных:", e)

        try:
            for row in range(self.stud_tableWidget.rowCount()):
                id = self.stud_tableWidget.item(row, 0).text()
                fio = self.stud_tableWidget.item(row, 1).text()
                frame = self.stud_tableWidget.item(row, 2).text()
                room = self.stud_tableWidget.item(row, 3).text()

                with connection.cursor() as cursor:
                    cursor.execute("SELECT fio, frame, room FROM stud WHERE id = %s", (id,))
                    original_fio, original_frame, original_room = cursor.fetchone()

                    # Обновляем запись в базе данных
                if fio != original_fio or frame != original_frame or room != original_room:
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE stud SET fio = %s, frame = %s, room = %s WHERE id = %s", (fio, frame, room, id))
            connection.commit()
        except Exception as a:
            print("Данные не изменены")

    def save_work(self):
        try:
            for row in range(self.work_tableWidget.rowCount()):
                id = self.work_tableWidget.item(row, 0).text()
                fio = self.work_tableWidget.item(row, 1).text()
                job_title = self.work_tableWidget.item(row, 2).text()
                frame_widget = self.work_tableWidget.cellWidget(row, 3)

                # Проверяем, что хотя бы одно из полей не пустое
                if frame_widget is not None:
                    frame = frame_widget.currentText() if frame_widget is not None else ""

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
                frame = self.work_tableWidget.item(row, 3).text()

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
                frame_widget = self.applications_tableWidget.cellWidget(row, 2)
                room_widget = self.applications_tableWidget.cellWidget(row, 3)
                fio_work_widget = self.applications_tableWidget.cellWidget(row, 4)
                job_title_widget = self.applications_tableWidget.cellWidget(row, 5)
                status_widget = self.applications_tableWidget.cellWidget(row, 7)


                description = self.applications_tableWidget.item(row, 6).text()
                if not description.strip():
                    QMessageBox.warning(MainWindow, "Ошибка", "Не введено описание для заявки.")
                    return

                # Проверяем, что хотя бы одно из полей не пустое
                if fio_stud_widget is not None or frame_widget is not None or room_widget is not None or fio_work_widget is not None or  job_title_widget is not None or status_widget:
                    fio_stud = fio_stud_widget.currentText() if fio_stud_widget is not None else ""
                    frame = frame_widget.currentText() if frame_widget is not None else ""
                    room = room_widget.currentText() if room_widget is not None else ""
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
            print("Данные сохранены в таблицу Работники.")
        except Exception as e:
            print("Ошибка при сохранении или редактировании данных:", e)

        try:
            for row in range(self.applications_tableWidget.rowCount()):
                id = self.applications_tableWidget.item(row, 0).text()
                fio_stud = self.applications_tableWidget.item(row, 1).text()
                frame = self.applications_tableWidget.item(row, 2).text()
                room = self.applications_tableWidget.item(row, 3).text()
                fio_work = self.applications_tableWidget.item(row, 4).text()
                job_title = self.applications_tableWidget.item(row, 5).text()
                description = self.applications_tableWidget.item(row, 6).text()
                status = self.applications_tableWidget.item(row, 7).text()

                with connection.cursor() as cursor:
                    cursor.execute("SELECT fio_stud, frame, room, fio_work, job_title, description, status FROM applications WHERE id = %s", (id,))
                    # original_fio, original_frame, original_room, original_room, original_room, original_room = cursor.fetchone()

                    # Обновляем запись в базе данных
                # if fio != original_fio or frame != original_frame or room != original_room:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE applications SET fio_stud = %s, frame = %s, room = %s, fio_work = %s,\
                job_title = %s, description = %s, status = %s WHERE id = %s", (fio_stud, frame, room, fio_work, job_title, description, status, id))
                # else:
                    # print("Данные не изменены")

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