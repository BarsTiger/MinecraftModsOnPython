from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block
import minecraftstuff as minecraftstuff
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
import time
import math
import random


def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

HOVER_HEIGHT = 15
ALIEN_TAUNTS = ["<àîȉɇĦЅ>Ti ne smozes ubegat veshno",
"<àîȉɇĦЅ>Soprotivlenie bespolzno!",
"<àîȉɇĦЅ>Mi vsevo lish hotim bit druzami"]


alienPos = mc.player.getTilePos()
alienPos.y = alienPos.y + 50
mode = "landing"

alienBlocks = [
minecraftstuff.ShapeBlock(-1,0,0, block.WOOL.id, 5),
minecraftstuff.ShapeBlock(0,0,-1, block.WOOL.id, 5),
minecraftstuff.ShapeBlock(1,0,0, block.WOOL.id, 5),
minecraftstuff.ShapeBlock(0,0,1, block.WOOL.id, 5),
minecraftstuff.ShapeBlock(0,-1,0, block.GLOWSTONE_BLOCK.id),
minecraftstuff . ShapeBlock(0,1,0,block.GLOWSTONE_BLOCK.id)]

alienShape = minecraftstuff.MinecraftShape(mc, alienPos, alienBlocks)

while mode != "missionaccomplished":
    playerPos = mc.player.getTilePos()
    if mode == "landing":
        mc.postToChat("<àîȉɇĦЅ>Mi prishli ne s mirom-pozaluysta, panikuyte!")
        alienTarget = playerPos.clone()
        alienTarget.y = alienTarget.y + HOVER_HEIGHT
        mode = "attack"
    elif mode == "attack":
        if alienPos.x == playerPos.x and alienPos.z == playerPos.z:
            mc.postToChat("<àîȉɇĦЅ>Teper ti nash! ")

            mc.setBlocks(0,50,0,6,56,6, block.BEDROCK.id)
            mc.setBlocks(1,51,1,5,55,5, block.AIR.id)
            mc.setBlock(3,55,3, block.GLOWSTONE_BLOCK.id)

            mc.player.setTilePos(3,51,5)
            time.sleep(20)
            mc.postToChat(" <àîȉɇĦЅ>ne samoe interesboe-otpravit nazad" )
            time.sleep(2)

            mc.player.setTilePos(playerPos.x, playerPos.y, playerPos.z)

            mc.setBlocks(0,50,0,6,56,6, block.AIR.id)
            mode = "missionaccomplished"

        else:
            mc.postToChat(ALIEN_TAUNTS[random.randint(0, len(ALIEN_TAUNTS) - 1)])
            alienTarget = playerPos.clone()
            alienTarget.y = alienTarget.y + HOVER_HEIGHT

    if alienPos != alienTarget:
        blocksBetween = mcdrawing.getLine(alienPos.x, alienPos.y, alienPos.z,alienTarget.x, alienTarget.y, alienTarget.z)

        for blockBetween in blocksBetween:
            alienShape.move(blockBetween.x, blockBetween.y, blockBetween.z)
            time.sleep(0.25)
        alienPos = alienTarget.clone()

alienShape.clear()

