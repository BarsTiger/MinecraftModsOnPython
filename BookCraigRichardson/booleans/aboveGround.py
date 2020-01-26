from mcpi.minecraft import Minecraft
mc = Minecraft.create()
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
highestBlockY = mc.getHeight(x, z)
aboveGround = y >= highestBlockY
print("highestBlock: " + str(highestBlockY) + " y:" + str(y))
mc.postToChat("Igrok nad zemloy? " + str(aboveGround))