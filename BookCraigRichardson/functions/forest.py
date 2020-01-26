from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    blockTypeDerevo = 17
    blockTypeLista = 161
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    y = y + 1
    mc.setBlock(x, y, z, blockTypeDerevo)
    dlinaNiza = 2
    shirinaNiza = 2
    visotaNiza = 1
    mc.setBlocks(x - 2, y, z - 2, x + dlinaNiza, y + visotaNiza, z + shirinaNiza, blockTypeLista)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
growTree(x + 6, y, z)
growTree(x + 12, y, z)
growTree(x + 18, y, z)
growTree(x + 24, y, z)
growTree(x + 30, y, z)
growTree(x + 36, y, z)
growTree(x + 42, y, z)