from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z + 1
dopoln = 0

block = int(input("Введите ID блока:   "))
estDopoln = int(input("У этого блока есть дополнительный идентификатор? Нет-0, есть-1    "))
if estDopoln != 0:
    dopoln = int(input("Тогда введите этот идентификатор:   "))

mc.setBlock(x, y, z, block, dopoln)