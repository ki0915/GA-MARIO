# 03. pyqt_paint_event.py
# PyQt Paint Event
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 300)
        self.setWindowTitle('GA Mario')
        self.show()

    # 창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)


        painter.setPen(QPen(Qt.black, 2.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.white))
        # 직사각형
        painter.drawRect(50, 7, 50, 50)

        painter.setPen(QPen(Qt.black, 2.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.white))
        # 직사각형
        painter.drawRect(0, 57, 50, 50)

        painter.setPen(QPen(Qt.black, 2.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.red))
        # 직사각형
        painter.drawRect(50, 57, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(Qt.black, 2.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.blue))
        # 직사각형
        painter.drawRect(0, 7, 50, 50)


        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(30, 180, 50, 240)


        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(60, 180, 60, 240)

        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(90, 180, 70, 240)
        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(QColor.fromRgb(0, 255, 0)))
        # 타원 그리기
        painter.drawEllipse(12, 160, 25, 25)

        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(90, 180, 70, 240)
        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.cyan))
        # RGB 색상으로 브러쉬 설정
        painter.drawEllipse(12, 160, 25, 25)



        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.white))
        # 타원 그리기
        painter.drawEllipse(47, 155, 25, 25)



        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.cyan))
        # 타원 그리기
        painter.drawEllipse(80, 160, 25, 25)

        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.gray))
        # 타원 그리기
        painter.drawEllipse(47, 237, 25, 25)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())