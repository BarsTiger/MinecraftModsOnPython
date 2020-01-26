from mcpi.minecraft import Minecraft
mc = Minecraft.create()

input("Подойдите к одному углу стираемой констукции и нажмите  ")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Подойдите к противоположному углу и нажмите   ")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

mc.setBlocks(x1, y1, z1, x2, y2, z2, 0)