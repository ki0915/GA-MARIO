#03. get_screen.py
#게임 화면 생성

import retro
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


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

        env.step()


        #창 띄우기
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())
