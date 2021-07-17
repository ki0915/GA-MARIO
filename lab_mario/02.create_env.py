#게임 환경 생상

import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

print(env)