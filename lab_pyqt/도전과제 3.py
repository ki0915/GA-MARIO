# 05.pyqt_timer.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 1

        #창의 크기 고정
        self.setFixedSize(324, 268)

        #창 제목
        self.setWindowTitle('GA Mario')

        self.text = QLabel(self)

        #타이머 생성
        qtimer = QTimer(self)
        #타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        qtimer.start(1000)

        #창 띄우기
        self.show()

    # 주기적으로 실행할 함수
    def timer(self):
        self.count = self.count + 1
        self.text.setText(str(self.count))
        self.text.setGeometry(100, 100, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())