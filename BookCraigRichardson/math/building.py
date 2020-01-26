from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
sirina = int(input("Ширина: "))
visota = int(input("Высота: "))
dlina = int(input("Длина: "))
blockType = int(input("Введите блок: "))
air = int(input("Чем заполнять постройку? (примеры ID: 0-воздух, 9-вода и тд"))
mc.setBlocks(x, y, z, x + sirina, y + visota, z + dlina, blockType )
mc.setBlocks(x + 1, y , z + 1, x + sirina - 1, y + visota - 1, z + dlina - 1, air )
