# this was thrown together in 30 minuites i couldnt figure out how to just get the hightmap from the save button and not all the bars so u gotta crop it
# yuhhh

import numpy as np
import matplotlib.pyplot as plt
from noise import snoise2

def generate_heightmap(size, scale=100.0, octaves=6, persistence=0.5, lacunarity=2.0):
    heightmap = np.zeros((size, size))
    for y in range(size):
        for x in range(size):
            nx = x / scale
            ny = y / scale
            value = snoise2(nx, ny, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
            value += np.random.uniform(-0.1, 0.1)
            heightmap[y][x] = value

    heightmap -= np.min(heightmap)
    heightmap /= np.max(heightmap)

    threshold = 2  # ??? idk what the hell im doin :skull:
    heightmap = np.where(heightmap > threshold, threshold, heightmap)

    heightmap = 0.5 * heightmap 

    return heightmap

map_size = 256  
my_heightmap = generate_heightmap(map_size)

plt.imshow(my_heightmap, cmap='gray', origin='lower')
plt.colorbar()
plt.show()
