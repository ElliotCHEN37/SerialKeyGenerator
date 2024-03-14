# main.py
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import random
import string


def generate_key(group_number, chars_per_group, include_special_chars, delimiter):
    key = ''
    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation

    for group in range(group_number):
        group_key = ''.join(random.choice(chars) for _ in range(chars_per_group))
        key += group_key
        if group < group_number - 1:
            key += delimiter

    return key


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(':/icon/icon.ico'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate_keys)

    def generate_keys(self):
        group_number = int(self.ui.lineEdit_8.text())
        chars_per_group = int(self.ui.lineEdit_6.text())
        include_special_chars = self.ui.comboBox_2.currentText() == "Yes"
        delimiter = self.ui.lineEdit_7.text()
        keys_to_generate = int(self.ui.lineEdit_5.text())

        with open("key.txt", "w") as file:
            for _ in range(keys_to_generate):
                generated_key = generate_key(group_number, chars_per_group, include_special_chars, delimiter)
                file.write(generated_key + "\n\n")

        print(f"{keys_to_generate} keys generated and saved to 'key.txt'.")
        self.setWindowTitle('Serial Key Generator - Keys saved to "key.txt"!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
