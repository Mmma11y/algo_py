from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from second_win import TestWin

# Previously in instr.py
txt_title = 'Health'
txt_hello = 'Welcome to the Health status detection program!'
txt_instruction = (
    'This application allows you to use the Rufier test to make an initial diagnosis of your health. '
    'Within 45 seconds, perform 30 squats, then measure your heart rate for the last 15 seconds of the first minute of recovery. '
    'Important: If you feel unwell during the test (e.g., dizziness), stop immediately.'
)
txt_next = 'Start'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

class MainWin(QWidget):
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
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

if __name__ == '__main__':
    app = QApplication([])
    mw = MainWin()
    app.exec_()
