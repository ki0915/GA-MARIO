#01. pyqt_basic.py
#pyqt 기본 가능

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #창의 크기 고정
        self.setFixedSize(1024, 768)

        #창 제목
        self.setWindowTitle('GA Mario')

        #창 띄우기
        self.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())

