from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 12
y = 72
z = -317
blockType = 52
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)




