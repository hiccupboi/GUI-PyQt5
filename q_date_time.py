import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):          #конструктор
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Date and Time', self)
        self.btn.move(55, 35)
        self.btn.clicked.connect(self.evt_btn_clicked)


    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfWeek())
        print(dt.dayOfYear())
        print(dt.addDays(21).toString())

        tm = QTime.currentTime()
        print(tm.toString())

        dtm = QDateTime.currentDateTime()
        print(dtm.toString())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
