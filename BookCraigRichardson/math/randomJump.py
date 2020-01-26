from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

x = x + random.randint(-100, 100)
y = y + random.randint(0, 100)
z = z + random.randint(-100, 100)
mc.player.setTilePos(x, y, z)