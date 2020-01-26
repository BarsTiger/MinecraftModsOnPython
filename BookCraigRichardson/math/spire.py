from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

visota = 3
blockType = 1

sideVisota = visota
mc.setBlocks(x + 1, y , z + 1, x + 3, y + sideVisota - 1, z + 3, blockType)

pointVisota = 5
mc.setBlocks(x + 2, y , z + 2, x + 2, y + pointVisota - 1, z + 2, blockType)

baseVisota = 1
mc.setBlocks(x, y , z, x + 4, y + baseVisota - 1, z + 4, blockType)