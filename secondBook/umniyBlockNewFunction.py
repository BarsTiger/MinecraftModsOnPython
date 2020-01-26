import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import minecraftstuff
mcdrawing = minecraftstuff.MinecraftDrawing(mc )
import mcpi.block as block
import time
import math
import random

def distanceBetweenPoints(pointl, point2) :
    xd = point2.x - pointl.x
    yd = point2.y - pointl.y
    zd = point2.z - pointl.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

TOO_FAR_AWAY = 15

blockMood = "happy"

friend = mc.player.getTilePos()
friend.x = friend.x + 5
friend.y = mc.getHeight(friend.x, friend.z)

mc.setBlock(friend.x, friend.y, friend . z, block.DIAMOND_BLOCK.id )

mc.postToChat("<block> Privet, drug :). Da, a almazniy block!")

target = friend.clone()

while True:
    pos = mc.player.getTilePos()
    distance = distanceBetweenPoints(pos, friend)

    if blockMood == "happy":
        if distance < TOO_FAR_AWAY:
            target = pos.clone()

        if distance >= TOO_FAR_AWAY:
            blockMood = "sad"
            mc.postToChat("<block> Vernis ko mne! Mne grustno:( Obnimi mena!(stan radom so mnoy)")

    elif blockMood == "sad":
        if distance <= 1:
            blockMood = "happy"
            mc.postToChat(" <block> Spasibo! Ti takoy klassniy:) Poshli dalshe")
        if random.randint(1, 100) == 100:
            blockMood = "hadenough"
            mc.postToChat("<block> Vse, hvatit. Ti mena brosaesh! A uhozhu ot teba! I bolshe ne razgovarivau")

    elif blockMood == "hadenough":
        if random.randint(1, 50) == 50:
            if distance <= 1:
                blockMood = "happy"
                mc.postToChat(" <block> ladno,spasibo! Ti takoy klassniy:) Poshli dalshe. A proshau vse obidi! ;)")

    if friend != target:
        blocksBetween = mcdrawing.getLine(friend.x, friend.y, friend.z, target.x, target.y, target.z)

        for blockBetween in blocksBetween[: -1]:
            mc.setBlock(friend.x, friend.y, friend.z, block.AIR.id)
            friend = blockBetween.clone()
            friend.y = mc.getHeight(friend.x, friend.z)
            mc.setBlock(friend.x, friend.y, friend.z,block.DIAMOND_BLOCK.id)
            time.sleep(0.25)
            target = friend.clone()
            
    time.sleep(0.25)