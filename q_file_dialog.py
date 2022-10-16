import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):  # конструктор
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Open File', self)
        self.btn.move(55, 35)
        self.btn.clicked.connect(self.evt_btn_file_open())

        self.btn = QPushButton('Save File', self)
        self.btn.move(55, 85)
        self.btn.clicked.connect(self.evt_btn_file_save())

    def evt_btn_file_open(self):
        res = QFileDialog.getOpenFileNames(self, 'Open File', 'Pictures/', 'JPG File (*.jpg)')
        print(res)

    def evt_btn_file_save(self):
        res = QFileDialog.getSaveFileName(self, 'Open File', 'Pictures/', 'JPG File (*.jpg)')
        print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
