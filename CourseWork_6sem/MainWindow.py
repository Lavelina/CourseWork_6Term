import os
import sys
import time

import main

from PyQt5.QtWidgets import QApplication, QBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.line_edit = None
        self.init_ui()
        self.resize(800, 300)
        k = main.AlphaNeumericVirtualKeyboard(self.line_edit)
        k.display(self.line_edit)

    def init_ui(self):
        self.line_edit = QLineEdit()
        self.layout = QVBoxLayout()
        self.layout.sizeHint()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.layout.addWidget(self.line_edit)
        self.setCentralWidget(self.main_widget)



app = QApplication(sys.argv)
mw = MainWindow()
mw.show()
sys.exit(app.exec_())