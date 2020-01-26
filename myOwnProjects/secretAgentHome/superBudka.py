from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import pickle
import time


def build(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in (row):
            for block in column:
                mc.setBlock(x, y, z, block)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart

def Del(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in (row):
            for block in column:
                mc.setBlock(x, y, z, 0)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart


file = open("perrysQartzBudka.txt", "rb")
structure = pickle.load(file)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

build(x, y, z, structure)


budX = x + 2
budY = y
budZ = z + 2

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

def perryVBudke(posx, posy, posz, budkX, budkZ):
    if posx == budkX and posz == budkZ:
        mc.setBlock(budkX - 1, posy, posz, 155)
        mc.setBlock(budkX - 1, posy + 1, posz, 155)
        time.sleep(2)
        mc.player.setTilePos(851, 67, -161)
    else:
        pos = mc.player.getTilePos()
        posx = pos.x
        posz = pos.z
        perryVBudke(posx, posy, posz, budkX, budkZ)

def domoy(posX, posY, posZ, tpX, tpY, tpZ, domX, domY, domZ):
    if posX == tpX and posY == tpY and posZ == tpZ:
        mc.player.setTilePos(domX, domY, domZ)
    else:
        pos = mc.player.getTilePos()
        posX = pos.x
        posY = pos.y
        posZ = pos.z
        domoy(posX, posY, posZ, tpX, tpY, tpZ, domX, domY, domZ)


perryVBudke(x, y, z, budX, budZ)
Del(x, y, z, structure)
domoy(x, y, z, 851, 67, -163, budX, budY, budZ)
