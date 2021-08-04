#06. get_full_screen_file.py
import numpy as np
import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()


# https://datacrystal.romhacking.net/wiki/Super_Mario_Bros.:RAM_map
#

full_screen_tiles = ram[0x0500:0x069F+1]

print(full_screen_tiles.shape)
print(full_screen_tiles)


full_screen_tiles_count = full_screen_tiles.shape[0]

full_screen_page1_tile = full_screen_tiles[:full_screen_tiles_count//2].reshape((13, 16))
full_screen_page2_tile = full_screen_tiles[full_screen_tiles_count//2:].reshape((13, 16))

full_screen_tile = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

print(full_screen_tile)