import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow


class GuessWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.num = random.randint(1, 99)
        self.ui.btn_check.clicked.connect(self.check_num)
        
    def check_num(self):
        guess_num = int(self.ui.word.value())
        if guess_num == self.num :
            a = QMessageBox(text="🫡🎉🎉!! You Win !!🎉🎉😍")
            self.num = random.randint(1, 99)
            self.ui.word.setValue(0)
        elif guess_num > self.num:
            a = QMessageBox(text="⬇️ Go Down! ⬇️")
        elif guess_num <self.num:
            a = QMessageBox(text="⬆️ Go Up! ⬆️")
        a.show()
        a.exec()

app = QApplication(sys.argv)
gn = GuessWord()
gn.show()
app.exec()