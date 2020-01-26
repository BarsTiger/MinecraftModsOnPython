from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y - 1, z)
notAir = str(blockType != 0)
mc.postToChat("Ne v vozduhe? " + notAir)