import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):          #конструктор
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Choose Color', self)
        self.btn.move(55, 35)
        self.btn.clicked.connect(self.evt_btn_color)


    def evt_btn_color(self):
        color = QColorDialog.getColor(QColor('#ffff00'), self, 'Choose Color')
        print(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
