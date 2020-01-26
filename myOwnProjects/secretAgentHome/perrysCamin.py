from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random
ranBlock = random.randint(1, 200)

parol = mc.getBlock(77, 93, 256)
parol2 = mc.getBlock(74, 93, 262)

while parol != 4 or parol2 != 4:
    parol = mc.getBlock(77, 93, 256)
    parol2 = mc.getBlock(74, 93, 262)
    if parol == 4 or parol2 == 4:
        mc.setBlock(78, 93, 259, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(78, 93, 258, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(77, 93, 258, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(77, 93, 259, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(76, 93, 258, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(76, 93, 259, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(76, 94, 258, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(76, 94, 259, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(77, 93, 256, ranBlock)
        ranBlock = random.randint(1, 200)
        mc.setBlock(74, 93, 262, ranBlock)

        time.sleep(2)

        mc.setBlock(78, 93, 259, 0)
        mc.setBlock(78, 93, 258, 0)
        mc.setBlock(77, 93, 258, 0)
        mc.setBlock(77, 93, 259, 0)
        mc.setBlock(76, 93, 258, 0)
        mc.setBlock(76, 93, 259, 0)
        mc.setBlock(76, 94, 258, 0)
        mc.setBlock(76, 94, 259, 0)
        mc.setBlock(77, 93, 256, 0)
        mc.setBlock(74, 93, 262, 0)
        break

time.sleep(3)

mc.setBlock(78, 93, 259, 44, 4)
mc.setBlock(78, 93, 258, 44, 4)
mc.setBlock(77, 93, 258, 51)
mc.setBlock(77, 93, 259, 51)
mc.setBlock(76, 93, 258, 45)
mc.setBlock(76, 93, 259, 45)
mc.setBlock(76, 94, 258, 45)
mc.setBlock(76, 94, 259, 45)


