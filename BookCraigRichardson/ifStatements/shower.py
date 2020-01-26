import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()


def diamondDoor(blockCode):
    mc.setBlock(94, 76, 339, blockCode)
    mc.setBlock(94, 77, 339, blockCode)


def openDoor():
    diamondDoor(0)


def closeDoor():
    diamondDoor(57)


shwrX1 = 93
shwrY1 = 76
shwrZ1 = 336

shwrX2 = 95
shwrY2 = 77
shwrZ2 = 337

pos = mc.player.getTilePos()


def shower():
    closeDoor()
    mc.setBlocks(shwrX1, shwrY1, shwrZ1, shwrX2, shwrY2, shwrZ2, 8)
    time.sleep(5)
    mc.setBlocks(shwrX1, shwrY1, shwrZ1, shwrX2, shwrY2, shwrZ2, 0)
    time.sleep(3)
    openDoor()


if shwrX1 <= pos.x <= shwrX2 and shwrY1 <= pos.y <= shwrY2 and shwrZ1 <= pos.z <= shwrZ2:
    shower()
else:
    mc.setBlocks(shwrX1, shwrY1, shwrZ1, shwrX2, shwrY2, shwrZ2, 0)
    mc.postToChat("Smotri console")
    input("Пожалуйста, войдите в душ и нажмите любую клавишу тут")
    shower()
