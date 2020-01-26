from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

places = int(input("Введите на сколько блоков будет распространяться освещение:   "))
kolvoBlocks = int(input("Введите, сколько блоков ставить:    "))

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z


for i in range(kolvoBlocks):
    type = kolvoBlocks/2
    place = random.randint(0 - places, places)
    if i <= type:
        blokx = x + place
        blokz = z - place
    else:
        blokx = x - place
        blokz = z + place
    bloky = mc.getHeight(x, z)
    mc.setBlock(blokx, bloky, blokz, 169)