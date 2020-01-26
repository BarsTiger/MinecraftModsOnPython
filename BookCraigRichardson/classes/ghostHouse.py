from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import  random

kolVo = int(input("Сколько раз появиться дом?  "))

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

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

ghostHouse = Building(x, y, z, 10, 6, 8)

def buildAndClear():

    ghostHouse.build()
    ghostHouse.buildDoor()
    ghostHouse.buildWindows()

    time.sleep(15)

    ghostHouse.clear()

    ghostHouse.x = random.randint(ghostHouse.x - 50, ghostHouse.x + 50)
    ghostHouse.z = random.randint(ghostHouse.z - 50, ghostHouse.z + 50)
    ghostHouse.y = mc.getHeight(ghostHouse.x, ghostHouse.z)


for i in range(kolVo):
    buildAndClear()
