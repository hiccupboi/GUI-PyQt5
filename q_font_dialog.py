import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):          #конструктор
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Choose Font', self)
        self.btn.move(55, 35)
        font = QFont('Arial', 14, 75, True)
        self.btn.setFont(font)
        self.btn.clicked.connect(self.evt_btn_clicked)


    def evt_btn_clicked(self):
        font, b_ok = QFontDialog.getFont()
        print(font, b_ok)
        if b_ok:
            self.btn.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
