#03. get_screen.py
#게임 화면 생성

import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')

#새 게임 시작

env.reset()

#화면 가져오기

screen = env.get_screen()

print(screen.shape)
print(screen)