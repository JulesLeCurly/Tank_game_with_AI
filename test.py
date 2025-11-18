import Function.core.Terrain as Terrain
import time

t = Terrain.Terrain(1200, 650, 500)

for i in range(2000):
    t.generate_terrain()
    time.sleep(1)