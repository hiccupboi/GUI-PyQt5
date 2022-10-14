import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):          #конструктор
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Input Name', self)
        self.btn.move(55, 35)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.btn = QPushButton('Show Input Age', self)
        self.btn.move(61, 85)
        self.btn.clicked.connect(self.evt_btn_age)

        self.btn = QPushButton('Show Input Colors', self)
        self.btn.move(53, 135)
        self.btn.clicked.connect(self.evt_btn_colors)


    def evt_btn_clicked(self):
        s_name, b_ok = QInputDialog.getText(self, 'Title', 'Enter your name:')
        if b_ok:
            QMessageBox.information(self, 'Name', 'Your name is ' + s_name)
        else:
            QMessageBox.critical(self, 'Canceled', 'You have clicked "Cancel"')

    def evt_btn_age(self):
        i_age, b_ok = QInputDialog.getInt(self, 'Title', 'Enter your age:', 18, 18, 80, 1)
        if b_ok:
            QMessageBox.information(self, 'Age', 'Your age is ' + str(i_age))
        else:
            QMessageBox.critical(self, 'Canceled', 'You have clicked "Cancel"')

    def evt_btn_colors(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
        s_color, b_ok = QInputDialog.getItem(self, 'Title', 'Enter your favorite color:', colors, editable=False)
        if b_ok:
            QMessageBox.information(self, 'Color', 'Your favorite color is ' + s_color)
        else:
            QMessageBox.critical(self, 'Canceled', 'You have clicked "Cancel"')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
