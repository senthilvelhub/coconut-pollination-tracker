from fileinput import filename
import sys
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTableView, QApplication, QWidget, QLineEdit, QFormLayout, QWidget, QPushButton, QVBoxLayout, QComboBox
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery,  QSqlTableModel
from DatabaseReader import DatabaseReader
from DatabaseTableWidget import VarietyTable
from PyQt5 import QtCore, QtGui, QtPrintSupport
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi("software.ui", self)

        self.database_entry_tab = self.findChild(QWidget, "tab")

        dr = DatabaseReader("sendb.db", "./DB/")
        # print(dr.get_table_names())

        # self.table_list = ["Variety", "Trees", "Workers"]
        self.table_list = dr.get_table_names()
        self.table_drop_down = QComboBox()
        self.table_drop_down.addItems(self.table_list)
        
        self.table_drop_down.adjustSize()
        self.table_drop_down.activated.connect(self.update_table_view)

        self.layout = QVBoxLayout()

        self.print_button = QPushButton('Print')
        self.print_button.clicked.connect(self.print)
        layout2 = QFormLayout()
        layout2.addRow('Choose Table', self.table_drop_down)
        layout2.addRow(self.print_button)
        self.layout.addLayout(layout2)

        # self.variety_table = VarietyTable()
        # layout.addWidget(self.variety_table)

        
        self.database_entry_tab.setLayout(self.layout)


        self.show()
    
    def update_table_view(self):
        item = self.layout.itemAt(1)
        if(item != None):
            widget = item.widget()
            widget.deleteLater()
        table_name = self.table_drop_down.currentText()
        self.model = QSqlTableModel()
        self.model.setTable(table_name)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange )
        self.model.select()
        # model.setHeaderData(0, Qt.Horizontal, "Name")
        # model.setHeaderData(1, Qt.Horizontal, "Salary")
        view = QTableView()
        view.setModel(self.model)
        # view.hideColumn(0) # don't show the ID
        # view.show()
        self.table_name = table_name
        self.layout.addWidget(view)
        # self.print_table(table_name, self.model)
       
        print(filename)

    def print(self):
        self.print_table(self.table_name, self.model)

    def print_table(self, table_name, model):
        now = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p").replace(":","")
        filename = f"{table_name}_{now}.pdf"
        # filename = f"table_{now}.pdf"
        # filename = "table2.pdf"
        # model = w.model()

        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setPaperSize(QtPrintSupport.QPrinter.A4)
        printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
        printer.setOutputFileName(filename)

        doc = QtGui.QTextDocument()

        html = """<html>
        <head>
        <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        </style>
        </head>"""
        html += "<table><thead>"
        html += "<tr>"
        for c in range(model.columnCount()):
            html += "<th>{}</th>".format(model.headerData(c, QtCore.Qt.Horizontal))

        html += "</tr></thead>"
        html += "<tbody>"
        for r in range(model.rowCount()):
            html += "<tr>"
            for c in range(model.columnCount()):
                html += "<td>{}</td>".format(model.index(r, c).data() or "")
            html += "</tr>"
        html += "</tbody></table>"
        doc.setHtml(html)
        doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
        doc.print_(printer)


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("DB/sendb.db")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
window = Window()
app.exec_()
