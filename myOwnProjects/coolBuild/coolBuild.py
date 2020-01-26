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


file = open("home.txt", "rb")
structure = pickle.load(file)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

build(x, y, z, structure)