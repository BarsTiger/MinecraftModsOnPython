from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 95
y = 80
z = 340
eda = 103
blockType = mc.getBlock(x, y, z)
noMelon = not blockType == eda
mc.postToChat("Nuzna eda: " + str(noMelon))