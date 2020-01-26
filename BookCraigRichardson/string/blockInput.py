from mcpi.minecraft import Minecraft
mc = Minecraft.create()
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
try:
    blockType = int (input('Введите номер блока:  '))
    mc.setBlock(x + 5, y, z + 5, blockType)
except:
    print("Это не число. Введите число")