# get_enemy_drawn.py

import retro


env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

enemy_drawn = ram[0x000F: 0x0013 + 1]

