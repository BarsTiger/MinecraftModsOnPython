from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

x2, y2, z2 = pos.x, pos.y, pos.z

mc.setBlocks(x, y, z, x + 4, y + 4, z + 4, 46)

for block in range(5):
    mc.setBlock(x + block, y + 4, z, 0)
    mc.setBlock(x, y + 4, z + block, 0)

x2, y2, z2 = x + 4, y, z + 4

for block2 in range(5):
    mc.setBlock(x2 - block2, y2 + 4, z2, 0)
    mc.setBlock(x2, y2 + 4, z2 - block2, 0)

for block3 in range(5):
    mc.setBlock(x + block3, y, z, 0)
    mc.setBlock(x, y, z + block3, 0)

x2, y2, z2 = x + 4, y, z + 4

for block4 in range(5):
    mc.setBlock(x2 - block4, y2, z2, 0)
    mc.setBlock(x2, y2, z2 - block4, 0)

mc.postToChat("Viydite iz blocka")
mc.postToChat("Posmotrite v konsol!")
input("Если хотите взорвать бомбу нажмите тут    ")
time.sleep(1)
mc.setBlock(x, y + 3, z, 152)