import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):          #конструктор
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show message', self)
        self.btn.move(55, 35)
        self.btn.clicked.connect(self.evt_btn_clicked)


    def evt_btn_clicked(self):
        # res = QMessageBox.information(self, 'Have a nice day', 'good day for coffee')
        # if res == QMessageBox.Ok:
        #     QMessageBox.information(self, ' ', 'I went to make coffee')
        msgDiskFull = QMessageBox()
        msgDiskFull.setText('Your hard drive is almost full')
        msgDiskFull.setDetailedText('Please free up disk space')
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setWindowTitle('Full Drive')
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
