from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

x = 97
y = 76
z = 342

x1 = 95
y1 = 64
z1 = 344

gift = mc.getBlock(x, y, z)
gift1 = mc.getBlock(x1, y1, z1)

if gift != 0 or gift1 != 0:
    mc.setBlock(95, 75, 341, 0)
    mc.setBlock(95, 63, 344, 0)
    mc.setBlock(95, 63, 343, 0)
    mc.setBlock(95, 64, 343, 0)
    mc.setBlock(95, 64, 344, 0)
    mc.setBlock(x, y, z, 0)
    time.sleep(10)
    mc.setBlock(95, 75, 341, 4)
    mc.setBlock(95, 63, 343, 57)
    mc.setBlock(95, 64, 343, 57)
    mc.setBlock(95, 63, 344, 57)
    mc.setBlock(92, 82, 340, random.randint(1, 200))
else:
    mc.setBlocks(97, 77, 340, 95, 77, 341, 10)
    mc.setBlocks(98, 66, 344, 89, 66, 346, 10)
    time.sleep(2)
    mc.setBlocks(97, 77, 340, 95, 77, 341, 0)
    mc.setBlocks(98, 66, 344, 89, 66, 346, 0)

