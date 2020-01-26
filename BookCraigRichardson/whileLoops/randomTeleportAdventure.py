from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

count = 0


while count < 10:
    x = random.randint(-1000, 1000)
    y = random.randint(20, 90)
    z = random.randint(-1000, 1000)
    mc.player.setTilePos(x, y, z)
    time.sleep(20)
    count += 1

mc.player.setTilePos(68, 87, 333)
