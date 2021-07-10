# 02. pyqt_widget.py
# pyqt 위젯 배치
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(400, 300)
        # 창 제목 설정
        self.setWindowTitle('MyApp')

        # 버튼
        button = QPushButton(self)
        button.setText('버튼')
        button.setGeometry(300, 200, 100, 100)

        # 텍스트
        self.label_text = QLabel(self)
        self.label_text.setText('가나다')
        self.label_text.setGeometry(180, 100, 50, 100)

        # 이미지
        label_image = QLabel(self)

        image = np.array([[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]])
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(100, 100, Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(-10, -45, 200, 200)

        # 창 띄우기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())


