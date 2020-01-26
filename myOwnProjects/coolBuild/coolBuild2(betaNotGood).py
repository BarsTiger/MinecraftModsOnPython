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
                time.sleep(0.07)
            x += 1
            z = zStart
        y += 1
        x = xStart

def buildTest(x, y, z, structure):
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

def buildDel(x, y, z, structure):
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


file = open("home.txt", "rb")
structure = pickle.load(file)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ans = 1

while ans != "ок" or ans != "ok":
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    buildTest(x, y, z, structure)
    time.sleep(1)
    buildDel(x, y, z, structure)
    ans = input("Если вы довольны постройкой и местом постройки введите ок. Если нет - нет или no     ")
    if ans == "нет" or ans == "no":
        buildDel(x, y, z, structure)
        break
    if ans == "ок" or ans == "ok":
        buildDel(x, y, z, structure)
        break


build(x, y, z, structure)