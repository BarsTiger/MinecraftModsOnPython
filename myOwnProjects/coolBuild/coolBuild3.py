from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import pickle
import time

nameNumber = int(input("Введите номер постройки, которую хотите: 1 - дом чуток хай-тек; 2 - 'коробка' про; 3 - деревенский дом; 4 - дом-куча нуба       "))
name = 0

if nameNumber == 1:
    name = "home.txt"
elif nameNumber == 2:
    name = "probox.txt"
elif nameNumber == 3:
    name = "vilage.txt"
elif nameNumber == 4:
    name = "noob.txt"


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


file = open(name, "rb")
structure = pickle.load(file)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

build(x, y, z, structure)