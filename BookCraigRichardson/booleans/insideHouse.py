from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

x1d1 = 92
y1d1 = 63
z1d1 = 341
x2d1 = 98
y2d1 = 87
z2d1 = 343

x1d2 = 95
y1d2 = 93
z1d2 = 324
x2d2 = 99
y2d2 = 96
z2d2 = 330

pos = mc.player.getTilePos()

time.sleep(1)

inside1 = (x1d1 <= pos.x <= x2d1) and (y1d1 <= pos.y <= y2d1) and (z1d1 <= pos.z <= z2d1)
inside2 = (x1d2 <= pos.x <= x2d2) and (y1d2 <= pos.y <= y2d2) and (z1d2 <= pos.z <= z2d2)
mc.postToChat("vnutri doma ? " + str(inside1 or inside2))