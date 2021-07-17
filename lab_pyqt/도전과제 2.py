# 04.pyqt_key_event.py
# pyqt 키 이벤트


from PyQt5.QtWidgets import QApplication, QWidget

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(324, 368)

        self.setWindowTitle('GA Mario')

        self.text = QLabel(self)
        self.text_1 = QLabel(self)

        self.show()


    # 키를 누를 때
    def keyPressEvent(self, event):
        key = event.key()
        self.text.setText(str(key) + "press")
        self.text.setGeometry(200, 300, 300, 50)


    # 키를 땔 때

    def keyReleaseEvent(self, event):
        key = event.key()

        self.text_1.setText(str(key) + "release")
        self.text_1.setGeometry(100, 200, 300, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())