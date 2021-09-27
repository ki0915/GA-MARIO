import retro
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor


relu = lambda x: np.maximum(0, x)
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))




class MyApp(QWidget):

    def __init__(self):
        self.height = 0
        self.width = 0
        self.paint_area = 20

        self.w1 = np.random.uniform(low=-1, high=1, size=(13 * 16, 9))
        self.b1 = np.random.uniform(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9, 6))
        self.b2 = np.random.uniform(low=-1, high=1, size=(6,))

        self.distance = 0
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0



        super().__init__()
        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 램 정보 가져오기


        # 새 게임 시작
        self.env.reset()
        # 화면 가져오기
        self.screen = self.env.get_screen()
        # 키 배열 B, NULL, SELECT, START, U, D, L, R, A
        self.button = [0, 0, 0, 0, 0, 0, 0, 0, 0]


        console_width = 428
        console_height = 480

        # 창의 크기 고정
        self.setFixedSize(1200, 480)

        # 창 제목
        self.setWindowTitle('GA Mario')

        self.label_image = QLabel(self)
        self.label_image.setGeometry(0, 0, console_width, console_height)


        # 타이머 생성
        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        qtimer.start(1000//60)
        # 창 띄우기
        self.show()

    def predict(self, data):
        l1 = relu(np.matmul(data, self.w1) + self.b1)
        output = sigmoid(np.matmul(l1, self.w2) + self.b2)
        result = (output > 0.5).astype(np.int)
        return result




    def keyPressEvent(self, event):
        key = event.key()

        # 위로 이동

        if key == Qt.Key_Up:
            self.button[4] = 1
        # 아래로 이동

        if key == Qt.Key_Down:
            self.button[5] = 1
        # 왼쪽으로 이동

        if key == Qt.Key_Left:
            self.button[6] = 1
        # 오른 쪽으로 이동

        if key == Qt.Key_Right:
            self.button[7] = 1
        # Z키
        if key == Qt.Key_Z:
            self.button[8] = 1
        # 달리기
        if key == Qt.Key_X:
            self.button[0] = 1


    def keyReleaseEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
                self.button[4] = 0

        if key == Qt.Key_Down:
                self.button[5] = 0

        if key == Qt.Key_Left:
                self.button[6] = 0

        if key == Qt.Key_Right:
                self.button[7] = 0

        if key == Qt.Key_Z:
                self.button[8] = 0

        if key == Qt.Key_X:
                self.button[0] = 0

    def update_screen(self):
        image = self.env.get_screen()
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(428, 480, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)



    def paintEvent(self, event):

        ram = self.env.get_ram()

        full_screen_tiles = ram[0x0500:0x069F + 1]

        full_screen_tiles_count = full_screen_tiles.shape[0]
        full_screen_page1_tile = full_screen_tiles[:full_screen_tiles_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tiles_count // 2:].reshape((13, 16))

        full_screen_tile = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)


        current_screen_page = ram[0x071A]
        # 0x071C	ScreenEdge X-Position, loads next screen when player past it?
        # 페이지 속 현재 화면 위치
        screen_position = ram[0x071C]

        # 화면 오프셋
        screen_offset = (256 * current_screen_page + screen_position) % 512
        # 타일 화면 오프셋
        screen_tile_offset = screen_offset // 16

        self.screen_current_tiles = np.concatenate((full_screen_tile, full_screen_tile), axis=1)[:,
                       screen_tile_offset:screen_tile_offset + 16]


        player_position_x = ram[0x03AD]

        # 0x03B8 Player y pos within current screen offset
        # 현재 화면 속 플레이어 y 좌표

        player_position_y = ram[0x03B8]

        # 타일 좌표로 변환
        player_tile_position_x = (player_position_x + 8) // 16
        player_tile_position_y = (player_position_y + 8) // 16 - 1



        enemy_horizon_position = ram[0x006E:0x0072 + 1]
        # 0x0087-0x008B	Enemy x position on screen
        # 자신이 속한 페이지 속 x 좌표
        enemy_screen_position_x = ram[0x0087:0x008B + 1]
        # 0x00CF-0x00D3	Enemy y pos on screen
        enemy_position_y = ram[0x00CF:0x00D3 + 1]
        # 적 x 좌표
        enemy_position_x = (enemy_horizon_position * 256 + enemy_screen_position_x) % 512



        enemy_drawn = ram[0x000F: 0x0013 + 1]

        # 적 타일 좌표
        enemy_tile_position_x = (enemy_position_x + 8) // 16
        enemy_tile_position_y = (enemy_position_y - 8) // 16 - 1


        painter = QPainter()

        painter.begin(self)


        # 맵 정보 출력

        for first_array in full_screen_tile:

            self.width = 0
            self.height += 20

            for second_array in first_array:


                if second_array == 0:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

                    painter.setBrush(QBrush(Qt.gray))

                    painter.drawRect(540 + self.width, 20 + self.height, self.paint_area, self.paint_area)

                    self.width += 20


                elif second_array == 84:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

                    painter.setBrush(QBrush(Qt.blue))

                    painter.drawRect(540 + self.width, 20 + self.height, self.paint_area, self.paint_area)

                    self.width += 20


                elif second_array == 192:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

                    painter.setBrush(QBrush(Qt.green))

                    painter.drawRect(540 + self.width, 20 + self.height, self.paint_area, self.paint_area)

                    self.width += 20


                elif second_array == 193:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

                    painter.setBrush(QBrush(Qt.darkYellow))

                    painter.drawRect(540 + self.width, 20 + self.height, self.paint_area, self.paint_area)

                    self.width += 20


                elif second_array == 6:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

                    painter.setBrush(QBrush(Qt.red))

                    painter.drawRect(540 + self.width, 20 + self.height, self.paint_area, self.paint_area)

                    self.width += 20



                else:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))

                    painter.setBrush(QBrush(Qt.blue))

                    painter.drawRect(540 + self.width, 20 + self.height, self.paint_area, self.paint_area)

                    self.width += 20




        for player_y in range(13):
            for player_x in range(16):
                if player_tile_position_x + screen_tile_offset > 31:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
                    painter.setBrush(QBrush(Qt.darkGray))
                    painter.drawRect(540 + ((player_tile_position_x + screen_tile_offset) - 32 ) * self.paint_area, 20 + (player_tile_position_y * self.paint_area) + 20, self.paint_area, self.paint_area)
                else:
                    painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
                    painter.setBrush(QBrush(Qt.darkGray))
                    painter.drawRect(540 + (player_tile_position_x + screen_tile_offset) * self.paint_area,
                                     20 + (player_tile_position_y * self.paint_area) + 20, self.paint_area,
                                     self.paint_area)
        for enemy in range(5):
            if enemy_drawn[enemy] != 0:
                painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(540 + (enemy_tile_position_x[enemy]) * self.paint_area, 20 + (enemy_tile_position_y[enemy] * self.paint_area) + 20, self.paint_area, self.paint_area)


    def AI_control(self):
        result = self.predict(self.screen_current_tiles.flatten())
        result = np.random.randint(0, 3, (13 * 16,), dtype=np.int)

        self.button[4] = result[0]
        # 아래로 이동


        self.button[5] = result[1]
        # 왼쪽으로 이동


        self.button[6] = result[2]
        # 오른 쪽으로 이동

        self.button[7] = result[3]
        # Z키

        self.button[8] = result[4]
        # 달리기

        self.button[0] = result[5]


    def timer(self):
        self.env.step(np.array(self.button))
        self.update_screen()
        self.update()
        self.height = 0
        self.AI_control()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())