from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

x = x + random.randint(-10, 10)
y = y + random.randint(0, 100)
z = z + random.randint(-10, 10)
mc.player.setTilePos(x, y, z)


blockType = random.randint(1, 200)
mc.setBlock(x, y - 1, z, blockType)

mc.postToChat("Tip bloka:" + str(blockType))
