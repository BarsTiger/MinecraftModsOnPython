import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

time.sleep(5)
mc.postToChat("Go!")

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

time.sleep(10)

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

xDist = x2 - x1
yDist = y2 - y1
zDist = z2 - z1

mc.postToChat("You moved on x: " + str(xDist) + ", y: " + str(yDist) + ", z: " + str(zDist))