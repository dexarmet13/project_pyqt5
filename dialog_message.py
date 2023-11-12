from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QColor
import sys


class Communicate(QObject):
    sendfromtodialog = pyqtSignal(object)

class Dialog_message(QDialog):
    def __init__(self, parent=None):
        super(Dialog_message, self).__init__(parent)
        self.communicate = Communicate

        self.setWindowTitle("Изменение цвета")

        self.layout = QVBoxLayout(self)
        self.label = QLabel("Изменение цвета Message")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.radio_button_layout = QHBoxLayout()
        self.layout.addLayout(self.radio_button_layout)

        colors = ["Красный", "Синий", "Зеленый", "Желтый", "Оранжевый"]
        self.radio_buttons = []

        for color_name in colors:
            radio_button = QRadioButton(color_name)
            self.radio_buttons.append(radio_button)
            self.radio_button_layout.addWidget(radio_button)

        self.button = QPushButton("Изменить фон")
        self.button.clicked.connect(self.change_background)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def change_background(self):
        selected_color = None

        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                selected_color = radio_button.text()
                break

        if selected_color:
            if selected_color == "Красный":
                color = QColor("red")
            elif selected_color == "Синий":
                color = QColor("blue")
            elif selected_color == "Зеленый":
                color = QColor("green")
            elif selected_color == "Желтый":
                color = QColor("yellow")
            elif selected_color == "Оранжевый":
                color = QColor("orange")

            # self.communicate.sendfromtodialog.emit(f"background-color: {color.name()};")

        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите цвет!")
