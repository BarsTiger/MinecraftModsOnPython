from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
import  random

kolVo = int(input("Сколько раз появиться гостиница?  "))


class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

    def build(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z + self.depth, 4)

        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,
                     self.x + self.width - 1, self.y + self.height - 1, self.z + self.depth - 1, 0)

        self.buildWindows()
        self.buildDoor()

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z + self.depth, 0)

    def buildWindows(self):
        mc.setBlock(self.x + (self.width / 4 * 3), self.y + 2, self.z, 95)
        mc.setBlock(self.x + (self.width / 4), self.y + 2, self.z, 95)

    def buildDoor(self):
        mc.setBlocks(self.x + (self.width / 2), self.y + 1, self.z, self.x + (self.width / 2), self.y + 2, self.z, 194)


class FancyBuilding(Building):
    def upgrade(self):

        mc.setBlocks(self.x + 1, self.y, self.z + 1,
                     self.x + self.width - 1, self.y, self.z + self.depth - 1,
                     35, 6)


        mc.setBlocks(self.x - 1, self.y, self.z - 1,
                     self.x - 1, self.y, self.z + self.depth + 1,
                     37)
        mc.setBlocks(self.x - 1, self.y, self.z - 1,
                     self.x + self.width + 1, self.y, self.z - 1,
                     37)
        mc.setBlocks(self.x + self.width + 1, self.y, self.z - 1,
                     self.x + self.width + 1, self.y, self.z + self.depth + 1,
                     37)
        mc.setBlocks(self.x - 1, self.y, self.z + self.depth + 1,
                     self.x + self.width + 1, self.y, self.z + self.depth + 1,
                     37)

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,self.x + self.width, self.y + self.height, self.z + self.depth, 0)

        mc.setBlocks(self.x - 1, self.y, self.z - 1,
                     self.x - 1, self.y, self.z + self.depth + 1,
                     0)
        mc.setBlocks(self.x - 1, self.y, self.z - 1,
                     self.x + self.width + 1, self.y, self.z - 1,
                     0)
        mc.setBlocks(self.x + self.width + 1, self.y, self.z - 1,
                     self.x + self.width + 1, self.y, self.z + self.depth + 1,
                     0)
        mc.setBlocks(self.x - 1, self.y, self.z + self.depth + 1,
                     self.x + self.width + 1, self.y, self.z + self.depth + 1,
                     0)


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostHotel = FancyBuilding(x, y, z, 10, 6, 8)

def buildAndClear():

    ghostHotel.build()
    ghostHotel.buildDoor()
    ghostHotel.buildWindows()
    ghostHotel.upgrade()

    time.sleep(15)

    ghostHotel.clear()

    ghostHotel.x = random.randint(ghostHotel.x - 50, ghostHotel.x + 50)
    ghostHotel.z = random.randint(ghostHotel.z - 50, ghostHotel.z + 50)
    ghostHotel.y = mc.getHeight(ghostHotel.x, ghostHotel.z)


for i in range(kolVo):
    buildAndClear()
