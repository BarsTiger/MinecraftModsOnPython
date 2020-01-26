from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

block = int(input("Введите ID блока, в который превратятся ударённые вами блоки(103-арбуз, 57-алмаз и т.д.)  "))

time.sleep(10)

hits = mc.events.pollBlockHits()


for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.setBlock(x, y, z, block)
