import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery,  QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)

class VarietyTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowTitle("QTableView Example")
        # self.resize(450, 250)
        # Set up the view and load the data
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["VarietyCode", "Name", "IsMale"])

        # self.view = QTableWidget()
        # self.view.setColumnCount(3)
        # self.view.setHorizontalHeaderLabels(["VarietyCode", "Name", "IsMale"])
        query = QSqlQuery("SELECT VarietyCode, Name, IsMale FROM Variety")

        while query.next():
            rows = self.rowCount()
            self.setRowCount(rows + 1)
            self.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
        self.resizeColumnsToContents()
        # self.setCentralWidget(self.view)



# app = QApplication(sys.argv)

# table = VarietyTable()
# table.show()
# sys.exit(app.exec_())