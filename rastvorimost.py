import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDialog, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QFont, QPalette
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1050, 600)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('проект')
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("ЭТО ТАБЛИЦА РАСТВОРИМОСТИ\n ЧТОБЫ УВИДЕТЬ ТАБЛИЦУ НАЖМИТЕ НА КНОПКУ", self)
        self.label.resize(400, 100)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 15))
        self.label.setStyleSheet("color: white;")

        self.button = QPushButton("ТАБЛИЦА", self)
        self.button.setFont(QFont("Arial", 14))
        self.button.setStyleSheet("background-color: #FF1493; color: white;")
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.clicked.connect(self.show_rastorimost)

        self.resizeEvent(None)

    def show_rastorimost(self):
        self.dialog = Rastvorimost(self)
        self.dialog.show()
        # self.hide()
        self.setVisible(True)  # Скрываем начальное окно
        self.dialog.exec_()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(127, 0, 128))

    def resizeEvent(self, event):
        label_width = self.width() // 2 + 100
        label_height = 100
        label_x = (self.width() - label_width) // 2
        label_y = (self.height() - label_height) // 2 - 50
        self.label.setGeometry(label_x, label_y, label_width, label_height)

        button_width = self.width() // 4
        button_height = 50
        button_x = (self.width() - button_width) // 2
        button_y = (self.height() - button_height) // 2 + 50
        self.button.setGeometry(button_x, button_y, button_width, button_height)


class Rastvorimost(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('project.ui', self)  # Загружаем дизайн
        self.main_window = mainWindow
        self.initUI()
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        style = QPalette()
        style.setColor(QPalette.Background, QColor(1, 28, 23))

        self.setPalette(style)
        self.ion_label.setStyleSheet("color: white")

        # self.ion_label.setStyleSheet("background-color: #14c8ff")
        self.solubility_label.setStyleSheet("color: white; border: 1px solid black; padding: 10px;")

    def initUI(self):
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

        self.btn_lst = [getattr(self, f"btn{i}") for i in range(1, 73)]

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
            message_box.setText(data)
            message_box.exec_()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())