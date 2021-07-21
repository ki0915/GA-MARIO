import retro
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer


env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')

#새 게임 시작

env.reset()

#화면 가져오기

screen = env.get_screen()

print(screen.shape)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #창의 크기 고정
        self.setFixedSize(428, 480)

        #창 제목
        self.setWindowTitle('GA Mario')

        label_image = QLabel(self)
        image = np.array(screen)
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(428, 480, Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0, 0, 428, 480)


        # 키 배열 B, NULL, SELECT, START, U, D, L, R, A
        env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))

        # 타이머 생성
        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        qtimer.start(1000)



        # 창 띄우기
        self.show()

    def update_screen(self):
        label_image = QLabel(self)
        image = np.array(screen)
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(428, 480, Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0, 0, 428, 480)


    def timer(self):
        self.env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.update_screen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())


