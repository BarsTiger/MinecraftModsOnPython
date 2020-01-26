from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

def makeMelon(pos, x, y, z):
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y - 1
    z = pos.z
    mc.setBlock(x, y, z, 103)
    time.sleep(5)

pos = mc.player.getPos()
x = pos.x
y = pos.y - 1
z = pos.z

makeMelon(pos, x, y, z)
makeMelon(pos, x, y, z)
makeMelon(pos, x, y, z)
makeMelon(pos, x, y, z)
makeMelon(pos, x, y, z)
makeMelon(pos, x, y, z)
