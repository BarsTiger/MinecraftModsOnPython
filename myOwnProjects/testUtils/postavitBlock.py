from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z + 1

blockType = int(input("Введите ID блока, который хотите поставить:      "))
mc.setBlock(x, y, z, blockType)