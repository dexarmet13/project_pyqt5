import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont, QPalette, QIcon
from PyQt5.QtCore import Qt, QFile
from rastvorimost import Rastvorimost


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
        self.setVisible(True)  # Скрываем начальное окно

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

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_F4:
                self.close()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.setWindowIcon(QIcon("d_cube_scan_icon_257072.png"))
    sys.exit(app.exec_())
