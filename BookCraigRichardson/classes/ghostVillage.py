from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import  random

kolVo = int(input("Сколько раз появиться поселок?  "))

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
shop = Building(x + 12, y, z, 8, 12, 10)
scaryHouse = Building(x + 24, y, z, 5, 30, 5)
castle = Building(x + 36, y, z, 10, 16, 16)

def buildAndClear():

    ghostHouse.build()
    ghostHouse.buildDoor()
    ghostHouse.buildWindows()

    shop.build()
    shop.buildDoor()
    shop.buildWindows()

    scaryHouse.build()
    scaryHouse.buildDoor()
    scaryHouse.buildWindows()

    castle.build()
    castle.buildDoor()
    castle.buildWindows()

    time.sleep(15)

    ghostHouse.clear()
    shop.clear()
    scaryHouse.clear()
    castle.clear()

    ghostHouse.x = random.randint(ghostHouse.x - 50, ghostHouse.x + 50)
    ghostHouse.z = random.randint(ghostHouse.z - 50, ghostHouse.z + 50)
    ghostHouse.y = mc.getHeight(ghostHouse.x, ghostHouse.z)

    shop.x = random.randint(shop.x - 50, shop.x + 50)
    shop.z = random.randint(shop.z - 50, shop.z + 50)
    shop.y = mc.getHeight(shop.x, shop.z)

    scaryHouse.x = random.randint(scaryHouse.x - 50, scaryHouse.x + 50)
    scaryHouse.z = random.randint(scaryHouse.z - 50, scaryHouse.z + 50)
    scaryHouse.y = mc.getHeight(scaryHouse.x, scaryHouse.z)

    castle.x = random.randint(castle.x - 50, castle.x + 50)
    castle.z = random.randint(castle.z - 50, castle.z + 50)
    castle.y = mc.getHeight(castle.x, castle.z)


for i in range(kolVo):
    buildAndClear()
