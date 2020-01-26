from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import shelve

def buildStructure(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in reversed(row):
            for block in column:
                mc.setBlock(x, y, z, block)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart

name = input("Введите название конструкции, которую хотите построить   ")

superBuildsFile = shelve.open("superBuildsFile.db")
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildStructure(x, y, z, superBuildsFile[name])