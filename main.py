import sys
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
from pyname import Ui_MainWindow
from pyname2 import Ui_MainWindow2


con = sqlite3.connect('./release/data/coffee.sqlite')

cur = con.cursor()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.display_coffee()

        self.pushButton.clicked.connect(self.editing)

    def display_coffee(self):
        result = cur.execute("SELECT * FROM specifications").fetchall()

        self.tableWidget.setRowCount(len(result))

        for row, row_data in enumerate(result):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row, col, item)

    def editing(self):
        self.second_form = EditCoffee()
        self.second_form.show()


class EditCoffee(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffee.sqlite")

        self.model = QSqlTableModel(self)
        self.model.setTable("specifications")
        self.model.select()

        self.view = QTableView(self)
        self.view.setModel(self.model)

        self.view.move(40, 30)
        self.view.resize(721, 201)

        self.pushButton.clicked.connect(self.updateDatabase)
        self.pushButton_2.clicked.connect(self.addRecord)

    def updateDatabase(self):
        self.model.submitAll()

    def addRecord(self):
        self.model.insertRow(self.model.rowCount())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())