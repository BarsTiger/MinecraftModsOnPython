from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

podhoditID = [57, 7, 103, 56, 5, 15, 48, 3, 47, 49, 16, 35]

block = random.choice(podhoditID)

pos = mc.player.getTilePos()

mc.setBlock(pos.x + 1, pos.y, pos.z + 1, block)



