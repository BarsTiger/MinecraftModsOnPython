from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

cube = [[[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]]]

startingX, startingY = x, y

for depth in cube:
    for heigth in reversed(depth):
        for block in heigth:
            mc.setBlock(x, y, z, block)
            x += 1
            time.sleep(0.1)
        y += 1
        x = startingX
    z += 1
    y = startingY
