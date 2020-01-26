from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()

stairBlock = 53

x, y, z = pos.x, pos.y, pos.z

dlina = int(input("Какой высоты будет лестница?  "))

for item in range(0, dlina):
    mc.setBlock(x + item, y + item, z, stairBlock)

input("Нажмите ENTER, чтобы удалить лестницу ")
for nomerDel in range(0, dlina):
    mc.setBlock(x + nomerDel, y + nomerDel, z, 0)


