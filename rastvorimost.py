import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt, QFile, QObject, pyqtSignal
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from dialog_message import Dialog_message


class Rastvorimost(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('project.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Таблица')
        self.initUI()
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        style = QPalette()
        style.setColor(QPalette.Background, QColor(1, 28, 23))

        self.setPalette(style)
        self.ion_label.setStyleSheet("color: white")
        self.solubility_label.setStyleSheet("color: white; border: 1px solid black; padding: 10px;")

        self.actionOpen.triggered.connect(self.open_explorer)
        self.actionClose.triggered.connect(self.close_project)
        self.actionInformation_2.triggered.connect(self.show_information)
        self.actionEdit_Message.triggered.connect(self.Edit_message)
        # self.actionEdit_Table.triggered.connect(self.Edit_table)
        self.dialog_message_run = Dialog_message()
        # self.dialog_message_run.communicate.sendfromtodialog.connect(self.get_var_dialog_message)

    def initUI(self):
        self.color_message = "background-color: white;"
        self.lst = ['Mg', 'Ca', 'Ba', 'Cu', 'Al', 'Fe', 'Ag', 'Zn']
        self.lst2 = ['CH3COO', 'OH', 'Cl', 'F', 'CO3', 'SO4', 'SiO3', 'PO4', 'SO3']
        self.label.setText("Mg<sup>2+</sup>")
        self.label.setStyleSheet("background-color: #14c8ff")

        self.label_2.setStyleSheet("background-color: #14c8ff")
        self.label_2.setText("Ca<sup>2+</sup>")

        self.label_3.setStyleSheet("background-color: #14c8ff")
        self.label_3.setText("Pb<sup>2+</sup>")

        self.label_4.setStyleSheet("background-color: #14c8ff")
        self.label_4.setText("Ba<sup>2+</sup>")

        self.label_5.setStyleSheet("background-color: #14c8ff")
        self.label_5.setText("Fe<sup>3+</sup>")

        self.label_6.setStyleSheet("background-color: #14c8ff")
        self.label_6.setText("Al<sup>3+</sup>")

        self.label_7.setStyleSheet("background-color: #14c8ff")
        self.label_7.setText("Ag<sup>+</sup>")

        self.label_8.setStyleSheet("background-color: #14c8ff")
        self.label_8.setText("Zn<sup>2+</sup>")

        self.label_9.setStyleSheet("background-color: #14c8ff")
        self.label_9.setText("OH<sup>-</sup>")

        self.label_10.setStyleSheet("background-color: #14c8ff")
        self.label_10.setText("Cl<sup>-</sup>")

        self.label_11.setStyleSheet("background-color: #14c8ff")
        self.label_11.setText("F<sup>-</sup>")

        self.label_12.setStyleSheet("background-color: #14c8ff")
        self.label_12.setText("CH<sub>3</sub>COO<sup>-</sup>")

        self.label_13.setStyleSheet("background-color: #14c8ff")
        self.label_13.setText("CO<sub>3</sub><sup>2-</sup>")

        self.label_14.setStyleSheet("background-color: #14c8ff")
        self.label_14.setText("SO<sub>4</sub><sup>2-</sup>")

        self.label_15.setStyleSheet("background-color: #14c8ff")
        self.label_15.setText("SO<sub>3</sub><sup>2-</sup>")

        self.label_16.setStyleSheet("background-color: #14c8ff")
        self.label_16.setText("SiO<sub>3</sub><sup>2-</sup>")

        self.label_17.setStyleSheet("background-color: #14c8ff")
        self.label_17.setText("PO<sub>4</sub><sup>3-</sup>")

        self.solubility_label.setStyleSheet("border: 1px solid black; padding: 10px;")
        self.buttonGroup.setExclusive(False)
        self.button_names = [button for button in self.buttonGroup.buttons()]

        self.solubilityTrue = [self.btn4, self.btn13, self.btn22, self.btn31, self.btn40, self.btn49, self.btn58,
                               self.btn67, self.btn28, self.btn2, self.btn11, self.btn29, self.btn38, self.btn47,
                               self.btn65, self.btn57, self.btn6, self.btn42, self.btn51, self.btn69]
        self.solubilityFalse = [self.btn71, self.btn17, self.btn26, self.btn35, self.btn8, self.btn9, self.btn18,
                                self.btn27, self.btn36, self.btn45, self.btn54, self.btn63,
                                self.btn72, self.btn64, self.btn37, self.btn46, self.btn56, self.btn3, self.btn12,
                                self.btn21, self.btn33, self.btn7, self.btn25, self.btn34, self.btn61, self.btn70,
                                self.btn39, self.btn14, self.btn23, self.btn32, self.btn68]
        self.solubility50_50 = [self.btn1, self.btn16, self.btn5, self.btn66, self.btn48, self.btn59, self.btn10,
                                self.btn19,
                                self.btn20, self.btn30, self.btn15, self.btn24, self.btn60]
        # self.button_names[1].setStyleSheet("background-color: red")
        for i in range(0, 72):
            if self.button_names[i] in self.solubilityTrue:
                self.button_names[i].setStyleSheet('QPushButton {background-color: #FFDB8B}')
                self.button_names[i].setText("Р")
            elif self.button_names[i] in self.solubilityFalse:
                self.button_names[i].setStyleSheet('QPushButton {background-color: #7f0f0f}')
                self.button_names[i].setText("Н")
            elif self.button_names[i] in self.solubility50_50:
                self.button_names[i].setStyleSheet('QPushButton {background-color: #F4A900}')
                self.button_names[i].setText("М")
            else:
                self.button_names[i].setText("-")

        self.btn1.clicked.connect(self.read_data_from_db)
        self.btn2.clicked.connect(self.read_data_from_db)
        self.btn3.clicked.connect(self.read_data_from_db)
        self.btn4.clicked.connect(self.read_data_from_db)
        self.btn5.clicked.connect(self.read_data_from_db)
        self.btn6.clicked.connect(self.read_data_from_db)
        self.btn7.clicked.connect(self.read_data_from_db)
        self.btn8.clicked.connect(self.read_data_from_db)
        self.btn9.clicked.connect(self.read_data_from_db)
        self.btn10.clicked.connect(self.read_data_from_db)
        self.btn11.clicked.connect(self.read_data_from_db)
        self.btn12.clicked.connect(self.read_data_from_db)
        self.btn13.clicked.connect(self.read_data_from_db)
        self.btn14.clicked.connect(self.read_data_from_db)
        self.btn15.clicked.connect(self.read_data_from_db)
        self.btn16.clicked.connect(self.read_data_from_db)
        self.btn17.clicked.connect(self.read_data_from_db)
        self.btn18.clicked.connect(self.read_data_from_db)
        self.btn19.clicked.connect(self.read_data_from_db)
        self.btn20.clicked.connect(self.read_data_from_db)
        self.btn21.clicked.connect(self.read_data_from_db)
        self.btn22.clicked.connect(self.read_data_from_db)
        self.btn23.clicked.connect(self.read_data_from_db)
        self.btn24.clicked.connect(self.read_data_from_db)
        self.btn25.clicked.connect(self.read_data_from_db)
        self.btn26.clicked.connect(self.read_data_from_db)
        self.btn27.clicked.connect(self.read_data_from_db)
        self.btn28.clicked.connect(self.read_data_from_db)
        self.btn29.clicked.connect(self.read_data_from_db)
        self.btn30.clicked.connect(self.read_data_from_db)
        self.btn31.clicked.connect(self.read_data_from_db)
        self.btn32.clicked.connect(self.read_data_from_db)
        self.btn33.clicked.connect(self.read_data_from_db)
        self.btn34.clicked.connect(self.read_data_from_db)
        self.btn35.clicked.connect(self.read_data_from_db)
        self.btn36.clicked.connect(self.read_data_from_db)
        self.btn37.clicked.connect(self.read_data_from_db)
        self.btn38.clicked.connect(self.read_data_from_db)
        self.btn39.clicked.connect(self.read_data_from_db)
        self.btn40.clicked.connect(self.read_data_from_db)
        self.btn41.clicked.connect(self.read_data_from_db)
        self.btn42.clicked.connect(self.read_data_from_db)
        self.btn43.clicked.connect(self.read_data_from_db)
        self.btn44.clicked.connect(self.read_data_from_db)
        self.btn45.clicked.connect(self.read_data_from_db)
        self.btn46.clicked.connect(self.read_data_from_db)
        self.btn47.clicked.connect(self.read_data_from_db)
        self.btn48.clicked.connect(self.read_data_from_db)
        self.btn49.clicked.connect(self.read_data_from_db)
        self.btn50.clicked.connect(self.read_data_from_db)
        self.btn51.clicked.connect(self.read_data_from_db)
        self.btn52.clicked.connect(self.read_data_from_db)
        self.btn53.clicked.connect(self.read_data_from_db)
        self.btn54.clicked.connect(self.read_data_from_db)
        self.btn55.clicked.connect(self.read_data_from_db)
        self.btn56.clicked.connect(self.read_data_from_db)
        self.btn57.clicked.connect(self.read_data_from_db)
        self.btn58.clicked.connect(self.read_data_from_db)
        self.btn59.clicked.connect(self.read_data_from_db)
        self.btn60.clicked.connect(self.read_data_from_db)
        self.btn61.clicked.connect(self.read_data_from_db)
        self.btn62.clicked.connect(self.read_data_from_db)
        self.btn63.clicked.connect(self.read_data_from_db)
        self.btn64.clicked.connect(self.read_data_from_db)
        self.btn65.clicked.connect(self.read_data_from_db)
        self.btn66.clicked.connect(self.read_data_from_db)
        self.btn67.clicked.connect(self.read_data_from_db)
        self.btn68.clicked.connect(self.read_data_from_db)
        self.btn69.clicked.connect(self.read_data_from_db)
        self.btn70.clicked.connect(self.read_data_from_db)
        self.btn71.clicked.connect(self.read_data_from_db)
        self.btn72.clicked.connect(self.read_data_from_db)
        self.btn1.setCursor(Qt.PointingHandCursor)
        self.btn2.setCursor(Qt.PointingHandCursor)
        self.btn3.setCursor(Qt.PointingHandCursor)
        self.btn4.setCursor(Qt.PointingHandCursor)
        self.btn5.setCursor(Qt.PointingHandCursor)
        self.btn6.setCursor(Qt.PointingHandCursor)
        self.btn7.setCursor(Qt.PointingHandCursor)
        self.btn8.setCursor(Qt.PointingHandCursor)
        self.btn9.setCursor(Qt.PointingHandCursor)
        self.btn10.setCursor(Qt.PointingHandCursor)
        self.btn11.setCursor(Qt.PointingHandCursor)
        self.btn12.setCursor(Qt.PointingHandCursor)
        self.btn13.setCursor(Qt.PointingHandCursor)
        self.btn14.setCursor(Qt.PointingHandCursor)
        self.btn15.setCursor(Qt.PointingHandCursor)
        self.btn16.setCursor(Qt.PointingHandCursor)
        self.btn17.setCursor(Qt.PointingHandCursor)
        self.btn18.setCursor(Qt.PointingHandCursor)
        self.btn19.setCursor(Qt.PointingHandCursor)
        self.btn20.setCursor(Qt.PointingHandCursor)
        self.btn21.setCursor(Qt.PointingHandCursor)
        self.btn22.setCursor(Qt.PointingHandCursor)
        self.btn23.setCursor(Qt.PointingHandCursor)
        self.btn24.setCursor(Qt.PointingHandCursor)
        self.btn25.setCursor(Qt.PointingHandCursor)
        self.btn26.setCursor(Qt.PointingHandCursor)
        self.btn27.setCursor(Qt.PointingHandCursor)
        self.btn28.setCursor(Qt.PointingHandCursor)
        self.btn29.setCursor(Qt.PointingHandCursor)
        self.btn30.setCursor(Qt.PointingHandCursor)
        self.btn31.setCursor(Qt.PointingHandCursor)
        self.btn32.setCursor(Qt.PointingHandCursor)
        self.btn33.setCursor(Qt.PointingHandCursor)
        self.btn34.setCursor(Qt.PointingHandCursor)
        self.btn35.setCursor(Qt.PointingHandCursor)
        self.btn36.setCursor(Qt.PointingHandCursor)
        self.btn37.setCursor(Qt.PointingHandCursor)
        self.btn38.setCursor(Qt.PointingHandCursor)
        self.btn39.setCursor(Qt.PointingHandCursor)
        self.btn40.setCursor(Qt.PointingHandCursor)
        self.btn41.setCursor(Qt.PointingHandCursor)
        self.btn42.setCursor(Qt.PointingHandCursor)
        self.btn43.setCursor(Qt.PointingHandCursor)
        self.btn44.setCursor(Qt.PointingHandCursor)
        self.btn45.setCursor(Qt.PointingHandCursor)
        self.btn46.setCursor(Qt.PointingHandCursor)
        self.btn47.setCursor(Qt.PointingHandCursor)
        self.btn48.setCursor(Qt.PointingHandCursor)
        self.btn49.setCursor(Qt.PointingHandCursor)
        self.btn50.setCursor(Qt.PointingHandCursor)
        self.btn51.setCursor(Qt.PointingHandCursor)
        self.btn52.setCursor(Qt.PointingHandCursor)
        self.btn53.setCursor(Qt.PointingHandCursor)
        self.btn54.setCursor(Qt.PointingHandCursor)
        self.btn55.setCursor(Qt.PointingHandCursor)
        self.btn56.setCursor(Qt.PointingHandCursor)
        self.btn57.setCursor(Qt.PointingHandCursor)
        self.btn58.setCursor(Qt.PointingHandCursor)
        self.btn59.setCursor(Qt.PointingHandCursor)
        self.btn60.setCursor(Qt.PointingHandCursor)
        self.btn61.setCursor(Qt.PointingHandCursor)
        self.btn62.setCursor(Qt.PointingHandCursor)
        self.btn63.setCursor(Qt.PointingHandCursor)
        self.btn64.setCursor(Qt.PointingHandCursor)
        self.btn65.setCursor(Qt.PointingHandCursor)
        self.btn66.setCursor(Qt.PointingHandCursor)
        self.btn67.setCursor(Qt.PointingHandCursor)
        self.btn68.setCursor(Qt.PointingHandCursor)
        self.btn69.setCursor(Qt.PointingHandCursor)
        self.btn70.setCursor(Qt.PointingHandCursor)
        self.btn71.setCursor(Qt.PointingHandCursor)
        self.btn72.setCursor(Qt.PointingHandCursor)

        self.btn_lst = [getattr(self, f"btn{i}") for i in range(1, 73)]

    def get_var_dialog_message(self, var):
        self.color_message = f"background-color: {var};"
    def read_from_db_convert(self, index):
        try:
            self.database_path = "solubility.db"
            self.conn = sqlite3.connect(self.database_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""SELECT info FROM solublis
                    WHERE button = {index}""")

            self.result = self.cursor.fetchone()[0]

            self.conn.close()
            return self.result
        except sqlite3.DatabaseError as error:
            self.statusBar().setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
            self.statusBar().showMessage(f"Ошибка при извлечении информации из базы данных: {str(error)}")
            return False

    def read_data_from_db(self, i):
        self.button_sender = self.sender()
        index = self.btn_lst.index(self.button_sender)
        data = self.read_from_db_convert(index)

        if data is not None:
            message_box = QMessageBox()
            message_box.setStyleSheet(self.color_message)
            message_box.setText(data)
            message_box.exec_()

    def open_explorer(self):
        url = QUrl.fromLocalFile('.')  # Путь к текущей директории
        QDesktopServices.openUrl(url)

    def close_project(self):
        self.close()

    def read_text_file_contents(self, file_path):
        file = QFile(file_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            text_stream = file.readAll()
            return str(text_stream, encoding='utf-8')
        else:
            QMessageBox.warning(self, 'Error', f'Could not open file: {file.errorString()}')

    def show_information(self, var):
        file_path = 'info_menubar.txt'  # Укажите ваш путь к файлу информации
        contents = self.read_text_file_contents(file_path)
        if contents:
            QMessageBox.information(self, 'Information', contents)

        else:
            QMessageBox.warning(self, 'Error', 'Could not read file contents.')

    def Edit_message(self):

        self.dialog_message_run.exec_()
