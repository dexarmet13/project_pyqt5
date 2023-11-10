from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox

from dialog_message_ui import Ui_MainWindow


class Dialog_message(QDialog, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
