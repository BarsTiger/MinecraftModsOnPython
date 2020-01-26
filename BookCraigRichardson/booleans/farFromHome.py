from mcpi.minecraft import Minecraft
import math

mc = Minecraft.create()

homeX = 95
homeZ = 341
dalekoOtDoma = 200

position = mc.player.getTilePos()
x = position.x
z = position.z

distance = math.sqrt((homeX - x) ** 2 + (homeZ - z) ** 2)
print(distance)
mc.postToChat("Player's home is near: " + str(distance <= dalekoOtDoma))
