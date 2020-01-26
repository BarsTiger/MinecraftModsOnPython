from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math
import time
import random

pos = mc.player.getTilePos()

destX = random.randint(pos.x - 127, pos.x + 127)
destZ = random.randint(pos.z - 127, pos.z + 127)
destY = mc.getHeight(destX, destZ)
block = 57

mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Block sozdan... Prikluchenie nachinaetsa!")

while True:
    pos = mc.player.getTilePos()
    distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)

    if distance > 100:
        mc.postToChat("Zamerznesh")
    elif distance > 50:
        mc.postToChat("Holodno")
    elif distance > 25:
        mc.postToChat("Teplo")
    elif distance > 12:
        mc.postToChat("Goracho")
    elif distance > 6:
        mc.postToChat("Obozzessa!")
    elif distance == 0:
        mc.postToChat("Pozdravlaem!!! Block nayden!")
        break
