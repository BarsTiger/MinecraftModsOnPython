from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import  random

buildingName = input("Как назовем замок? (только англ. буквами)   ")
kolVo = int(input("Сколько раз появиться замок?  "))

class NamedBuilding(object):
    def __init__(self, x, y, z, width, height, depth, name):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
        self.name = name
    def build(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + self.width, self.y + self.height, self.z + self.depth, 4)
        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1, self.x + self.width - 1, self.y + self.height - 1, self.z + self.depth - 1, 0)

    def buildDoor(self):
        mc.setBlocks(self.x + (self.width / 2), self.y + 1, self.z, self.x + (self.width / 2), self.y + 2, self.z, 0)

    def buildWindows(self):
        mc.setBlock(self.x + (self.width / 4 * 3), self.y + 2, self.z, 0)
        mc.setBlock(self.x + (self.width / 4), self.y + 2, self.z, 0)

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z, self.x + self.width, self.y + self.height, self.z + self.depth, 0)

    def getInfo(self):
        return self.name + " imeet koordinati " + str(self.x) + ", " + str(self.y) + ", " + str(self.z)

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

ghostBuilding = NamedBuilding(x, y, z, 10, 16, 16, buildingName)

def buildAndClear():

    ghostBuilding.build()
    ghostBuilding.buildDoor()
    ghostBuilding.buildWindows()

    mc.postToChat(ghostBuilding.getInfo())

    time.sleep(15)

    ghostBuilding.clear()

    ghostBuilding.x = random.randint(ghostBuilding.x - 50, ghostBuilding.x + 50)
    ghostBuilding.z = random.randint(ghostBuilding.z - 50, ghostBuilding.z + 50)
    ghostBuilding.y = mc.getHeight(ghostBuilding.x, ghostBuilding.z)


for i in range(kolVo):
    buildAndClear()
