from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import  random

kolVo = int(input("Сколько раз появиться дерево?  "))

class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
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



class Tree(Building):
    def build(self):
        wood = 17
        leaves = 18

        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 5, self.z, wood)

        mc.setBlocks(self.x - 2, self.y + 6, self.z - 2, self.x + 2, self.y + 6, self.z + 2, leaves)
        mc.setBlocks(self.x - 1, self.y + 7, self.z - 1, self.x + 1, self.y + 7, self.z + 1, leaves)

    def getInfo(self):
        return"Derevo imeet koordinati " + str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def clear(self):

        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 5, self.z, 0)


        mc.setBlocks(self.x - 2, self.y + 6, self.z - 2, self.x + 2, self.y + 6, self.z + 2, 0)
        mc.setBlocks(self.x - 1, self.y + 7, self.z - 1, self.x + 1, self.y + 7, self.z + 1, 0)


pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z


ghostTree = Tree(x, y, z, 10, 6, 8)


def buildAndClear():

    ghostTree.build()

    mc.postToChat(ghostTree.getInfo())
    print(ghostTree.getInfo())

    time.sleep(5)

    ghostTree.clear()

    ghostTree.x = random.randint(ghostTree.x - 20, ghostTree.x + 20)
    ghostTree.z = random.randint(ghostTree.z - 20, ghostTree.z + 20)
    ghostTree.y = mc.getHeight(ghostTree.x, ghostTree.z)


for i in range(kolVo):
    buildAndClear()
