import retro
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 램 정보 가져오기
        self.ram = self.env.get_ram()
        self.full_screen_tiles = self.ram[0x0500:0x069F + 1]

        # 새 게임 시작
        self.env.reset()
        # 화면 가져오기
        self.screen = self.env.get_screen()
        # 키 배열 B, NULL, SELECT, START, U, D, L, R, A
        self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 창의 크기 고정
        self.setFixedSize(1200, 480)

        # 창 제목
        self.setWindowTitle('GA Mario')

        self.label_image = QLabel(self)
        self.label_image.setGeometry(0, 0, 428, 480)

        # 타이머 생성
        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        qtimer.start(1000//60)
        # 창 띄우기
        self.show()

    def update_ram(self):
        full_screen_tiles_count = self.full_screen_tiles.shape[0]
        full_screen_page1_tile = self.full_screen_tiles[:full_screen_tiles_count // 2].reshape((13, 16))
        full_screen_page2_tile = self.full_screen_tiles[full_screen_tiles_count // 2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=0).astype(np.int)

        print(full_screen_tiles)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
            self.button = [0, 0, 0, 0, 1, 0, 0, 0, 0]

        if key == Qt.Key_Down:
            self.button = [0, 0, 0, 0, 0, 1, 0, 0, 0]

        if key == Qt.Key_Left:
            self.button = [0, 0, 0, 0, 0, 0, 1, 0, 0]

        if key == Qt.Key_Right:
            self.button = [0, 0, 0, 0, 0, 0, 0, 1, 0]

        if key == Qt.Key_Z:
            self.button = [0, 0, 0, 0, 0, 0, 0, 0, 1]

        if key == Qt.Key_X:
            self.button = [1, 0, 0, 0, 0, 0, 0, 0, 0]

    def keyReleaseEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
                self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if key == Qt.Key_Down:
                self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if key == Qt.Key_Left:
                self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if key == Qt.Key_Right:
                self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if key == Qt.Key_Z:
                self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        if key == Qt.Key_X:
                self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def update_screen(self):
        image = self.env.get_screen()
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(428, 480, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)



    def timer(self):
        self.env.step(np.array(self.button))
        self.update_ram()
        self.update_screen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())
