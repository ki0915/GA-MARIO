import numpy as np
import retro
from PyQt5.QtCore import QTimer

relu = lambda x: np.max(0, x)
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))
answer = 0

class Chromosome:


    def __init__(self):
        self.w1 = np.random.uniform(low=-1, high=1, size=(13 * 16, 9))
        self.b1 = np.random.random(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9, 6))
        self.b2 = np.random.random(low=-1, high=1, size=(6,))

        self.distance = 0
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0

        qtimer = QTimer(self)
        # 타이머에 실행할 함수 연결
        qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        qtimer.start(1000 // 60)



    def predict(self, data):
        l1 = relu(np.matmul(data, self.w1) + self.b1)
        output = sigmoid(np.matmul(l1, self.w2) + self.b2)
        result = (output > 0.5).astype(np.int)
        print(result)



    def current_file(self):
        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        env.reset()

        ram = env.get_ram()

        # https://datacrystal.romhacking.net/wiki/Super_Mario_Bros.:RAM_map
        # 0x0500-0x069F	Current tile (Does not effect graphics)
        full_screen_tiles = ram[0x0500:0x069F+1]

        full_screen_tile_count = full_screen_tiles.shape[0]

        full_screen_page1_tile = full_screen_tiles[:full_screen_tile_count//2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count//2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)



    # 0x071A	Current screen (in level)
    # 현재 화면이 속한 페이지 번호
        current_screen_page = ram[0x071A]
    # 0x071C	ScreenEdge X-Position, loads next screen when player past it?
    # 페이지 속 현재 화면 위치
        screen_position = ram[0x071C]
    # 화면 오프셋
        screen_offset = (256 * current_screen_page + screen_position) % 512
    # 타일 화면 오프셋
        screen_tile_offset = screen_offset // 16

    # 현재 화면 추출
        screen_tiles = np.concatenate((full_screen_tiles, full_screen_tiles), axis=1)[:, screen_tile_offset:screen_tile_offset+16]
        answer = screen_tiles

    def timer(self):
        self.current_file()
        self.predict(answer)
