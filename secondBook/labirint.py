from mcpi.minecraft import Minecraft as minecraft
mc = minecraft.create()
import mcpi.block as block
import minecraftstuff
import time
import random
import _thread
deltype = int(input("вы на земле или в воздухе? если на земле-введите 1, если в воздухе - 2       "))


ARENAX = 10
ARENAZ = 20
ARENAY = 3
def createArena(pos):
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1,pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1, block.GRASS.id)
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,block.GLASS.id)
    mc.setBlocks(pos.x, pos.y + 1, pos.z,pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ, block.AIR.id)

def delArena2(pos):
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1,pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1, block.AIR.id)
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,block.AIR.id)
    mc.setBlocks(pos.x, pos.y + 1, pos.z,pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ, block.AIR.id)

def delArena1(pos):
    mc.setBlocks(pos.x - 1, pos.y, pos.z - 1, pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1, block.GRASS.id)
    mc.setBlocks(pos.x - 1, pos.y, pos.z - 1,pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,block.AIR.id)
    mc.setBlocks(pos.x, pos.y + 1, pos.z,pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ, block.AIR.id)

def theWall(arenaPos, wallZPos):
    wallPos = mc.Vec3(arenaPos.x, arenaPos.y + 1, arenaPos.z + wallZPos)
    wallBlocks = []
    for x in range(0, ARENAX + 1):
        for y in range(1, ARENAY):
            wallBlocks.append(minecraftstuff.ShapeBlock(x, y, 0, block.BRICK_BLOCK.id))
    wallShape = minecraftstuff.MinecraftShape(mc, wallPos, wallBlocks)
    while not gameOver:
        wallShape.moveBy(0,1,0)
        time.sleep(1)
        wallShape.moveBy(0,-1,0)
        time.sleep(1)
def theRiver(arenaPos, riverZPos):
    RIVERWIDTH = 4
    BRIDGEWIDTH = 2
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,arenaPos.x + ARENAX, arenaPos.y,arenaPos.z + riverZPos + RIVERWIDTH - 1, block.AIR.id)
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,arenaPos.x + ARENAX, arenaPos.y - 2,arenaPos.z + riverZPos + RIVERWIDTH - 1, block.WATER.id)
    bridgePos = mc.Vec3(arenaPos.x, arenaPos.y, arenaPos.z + riverZPos + 1)
    bridgeBlocks = []
    for x in range(0, BRIDGEWIDTH):
        for z in range(0, RIVERWIDTH - 2):
            bridgeBlocks.append(minecraftstuff.ShapeBlock(x, 0, z, block.WOOD_PLANKS.id))
    bridgeShape = minecraftstuff.MinecraftShape(mc, bridgePos, bridgeBlocks)
    steps = ARENAX - BRIDGEWIDTH
    while not gameOver:
        for left in range(0, steps):
            bridgeShape.moveBy(1,0,0)
            time.sleep(1)
        for right in range(0, steps):
            bridgeShape.moveBy(-1,0,0)
            time.sleep(1)
def theHoles(arenaPos, holesZPos):

    HOLES = 15
    HOLESWIDTH = 3
    while not gameOver:

        holes = []
        for count in range(0,HOLES):
            x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
            z = random.randint(arenaPos.z + holesZPos,arenaPos.z + holesZPos + HOLESWIDTH)
            holes.append(mc.Vec3(x, arenaPos.y, z))
        for hole in holes:
            mc.setBlock(hole.x, hole.y, hole.z, block.WOOL.id, 15)
        time.sleep(0.25)
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,
            hole.x, hole.y - 2, hole.z, block.AIR.id)

        time.sleep(2)
        for hole in holes:
            mc.setBlocks(hole.x, hole.y, hole.z,hole.x, hole.y - 2, hole.z, block.GRASS.id)
        time.sleep(0.25)
def createDiamonds(arenaPos, number):
    for diamond in range(0, number):
        x = random.randint(arenaPos.x, arenaPos.x + ARENAX)
        z = random.randint(arenaPos.z, arenaPos.z + ARENAZ)
        mc.setBlock(x, arenaPos.y + 1, z, block.DIAMOND_BLOCK.id)
gameOver = False
arenaPos = mc.player.getTilePos()
createArena(arenaPos)
WALLZ = 10
_thread.start_new_thread(theWall, (arenaPos, WALLZ))
RIVERZ = 4
_thread.start_new_thread(theRiver, (arenaPos, RIVERZ))
HOLESZ = 15

_thread.start_new_thread(theHoles, (arenaPos, HOLESZ))

LEVELS = 3
DIAMONDS = [3,5,9]
TIMEOUTS = [30,25,20]
level = 0
points = 0
while not gameOver:
    createDiamonds(arenaPos, DIAMONDS[level])
    diamondsLeft = DIAMONDS[level]

    mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)
    start = time.time()
    levelComplete = False
    while not gameOver and not levelComplete:
        time.sleep(0.1)
        hits = mc.events.pollBlockHits()
        for hit in hits:
            blockHitType = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
            if blockHitType == block.DIAMOND_BLOCK.id:

                mc.setBlock(hit.pos.x,hit.pos.y, hit.pos.z, block.AIR.id)

                diamondsLeft = diamondsLeft - 1

        pos = mc.player.getTilePos()

        if pos.y < arenaPos.y:
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)

        if pos.z == arenaPos.z + ARENAZ and diamondsLeft == 0:
            levelComplete = True

        secondsLeft = TIMEOUTS[level] - (time.time() - start)
        if secondsLeft < 0:
            gameOver = True
            mc.postToChat("Vrema vislo...")

    if levelComplete:
        points = points + (DIAMONDS[level] * int(secondsLeft))
        mc.postToChat("Uroven proyden! Ochki - " + str(points))

        level = level + 1

        if level == LEVELS:
            gameOver = True
            mc.postToChat("Super! Ti proshol vse urovni")

mc.postToChat("Igra okonchena. Ochki - " + str(points))
time.sleep(1)
if deltype == 1:
    delArena1(arenaPos)
else:
    delArena2(arenaPos)

