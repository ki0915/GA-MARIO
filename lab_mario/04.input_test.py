#04.input_test.py
#게임에 입력 보내기

#03. get_screen.py
#게임 화면 생성

import retro
import numpy as np

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')

#새 게임 시작


#키 배열 B, NULL, SELECT, START, U, D, L, R, A

env.reset()

#키 배열 B, NULL, SELECT, START, U, D, L, R, A

env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0]))

#화면 가져오기

screen = env.get_screen()

print(screen.shape)
print(screen)