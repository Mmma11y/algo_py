from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from final_win import FinalWin

# Shared variables (used to be in instr.py)
txt_title = 'Health'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lbl_name = QLabel('Enter your full name:')
        self.txt_name = QLineEdit('Full name')
        self.lbl_age = QLabel('Enter your age:')
        self.txt_age = QLineEdit('Age')
        self.lbl_test1 = QLabel('Heart rate before test:')
        self.txt_test1 = QLineEdit('0')
        self.lbl_test2 = QLabel('Heart rate after squats:')
        self.txt_test2 = QLineEdit('0')
        self.lbl_test3 = QLabel('Heart rate after recovery:')
        self.txt_test3 = QLineEdit('0')

        self.lbl_instruction = QLabel('Perform 30 squats in 45 seconds, then measure heart rate.')
        self.btn_test = QPushButton('Start Test')

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.l_line.addWidget(self.lbl_name)
        self.l_line.addWidget(self.txt_name)
        self.l_line.addWidget(self.lbl_age)
        self.l_line.addWidget(self.txt_age)
        self.l_line.addWidget(self.lbl_test1)
        self.l_line.addWidget(self.txt_test1)
        self.l_line.addWidget(self.lbl_test2)
        self.l_line.addWidget(self.txt_test2)
        self.l_line.addWidget(self.lbl_test3)
        self.l_line.addWidget(self.txt_test3)

        self.r_line.addWidget(self.lbl_instruction)
        self.r_line.addWidget(self.btn_test)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_test.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
