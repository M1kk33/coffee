import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


con = sqlite3.connect('./coffee.sqlite')

cur = con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
        self.display_coffee()

    def display_coffee(self):
        result = cur.execute("SELECT * FROM specifications").fetchall()

        self.tableWidget.setRowCount(len(result))

        for row, row_data in enumerate(result):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row, col, item)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())