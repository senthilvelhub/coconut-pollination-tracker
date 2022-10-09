from calendar import c
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout, QWidget, QPushButton, QVBoxLayout, QComboBox


class Window(QWidget):
    def __init__(self, title, connection, parent=None):
        super().__init__(parent)
        self.initUI(title)
        self.connection = connection
        self.cursor = self.connection.cursor()

    def initUI(self, title):
        self.setWindowTitle(title)
        self.layout = QVBoxLayout()

        tree_varieties = ["1", "2", "3"]
        self.variety_drop_down = QComboBox()
       # self.variety_drop_down.addItems(tree_varieties)
       
        # self.variety_drop_down.addItems("1,"one")
        layout2 = QFormLayout()

        self.serial_number = QLineEdit()
        self.min_flower_time = QLineEdit()
        self.nut_growth_time = QLineEdit()

        layout2.addRow('Serial No.:', self.serial_number)
        layout2.addRow('Min. Flower Time:', self.min_flower_time)
        layout2.addRow('Variety', self.variety_drop_down)
        layout2.addRow('Nut Growth Time:', self.nut_growth_time)

        self.layout.addLayout(layout2)

        self.btn_submit = QPushButton('Submit')
        self.btn_submit.clicked.connect(self.submitData)
        self.btn_submit.setToolTip('This is puts an entry into tree database')

        self.layout.addWidget(self.btn_submit)

        self.setLayout(self.layout)

    def submitData(self):
        self.cursor.execute("INSERT INTO trees VALUES( 1, "
        +self.serial_number.text()+"," 
        + self.variety_drop_down.currentText() + "," 
        + self.min_flower_time.text() + ","
        + self.nut_growth_time.text() +")")
        print("INSERT INTO trees VALUES( 1, "
        +self.serial_number.text()+"," 
        + self.variety_drop_down.currentText() + "," 
        + self.min_flower_time.text() + ","
        + self.nut_growth_time.text() + ")")
        
        self.connection.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    connection = sqlite3.connect('tree.db')
    window = Window("Data Entry", connection)
    window.show()
    ret = app.exec()
    connection.close()
    sys.exit(ret)
