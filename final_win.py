from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

# Shared variables (used to be in instr.py)
txt_title = 'Health'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lbl_result = QLabel('Rufier Index: 0')
        self.lbl_performance = QLabel('Cardiac performance: No data for the age')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_result)
        self.layout.addWidget(self.lbl_performance)
        self.setLayout(self.layout)
