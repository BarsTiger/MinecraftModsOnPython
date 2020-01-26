from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0
pos = mc.player.getTilePos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    pos = mc.player.getPos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    score = score + 1
    mc.postToChat("Tecushiy schet: " + str(score) + ", Ti smozes!")

mc.postToChat("Okonchatelnyy schet: " + str(score) + ", Ti molodes!")

if score > 6:
    finalPos = mc.player.getTilePos()
    mc.postToChat("Ti dolgo sidel pod vodoy! Vot tebe svetocniy dozd!")
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5, finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
