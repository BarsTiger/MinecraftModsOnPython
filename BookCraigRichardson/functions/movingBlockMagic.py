from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

block = 0
sleep = 0

answerBlock = int(input("Какой блок будет ходить? 1-светильник Джека, 2-алмазный блок, 3-верстак, 4-динамит, 5-замшелый булыжник, "
                    "6-редстоун блок, 7-саженец дуба, 8-сундук, 9-яйцо дракона, 10-кровать  "))
if answerBlock == 1:
    block = 91
elif answerBlock == 2:
    block = 51
elif answerBlock == 3:
    block = 58
elif answerBlock == 4:
    block = 46
elif answerBlock == 5:
    block = 48
elif answerBlock == 6:
    block = 152
elif answerBlock == 7:
    block = 6
elif answerBlock == 8:
    block = 54
elif answerBlock == 9:
    block = 122
elif answerBlock == 10:
    block = 26

prType = int(input("Как будет перемещаться блок? 1-ровно и красиво(но есть ловушки, которые он не пройдет) 2-по диагонали, но проходит все ловушки  "))

answerSpeed = int(input("Как будет перемещаться блок? 1-медленно, 2-быстро, 3-очень быстро  "))
if answerSpeed == 1:
    sleep = 1
elif answerSpeed == 2:
    sleep = 0.5
elif answerSpeed == 3:
    sleep = 0.1



def calculateMove(programType):
    global x
    global y
    global z

    currentHeight = mc.getHeight(x, z) - 1

    forwardHeight = mc.getHeight(x + 1, z)
    rightHeight = mc.getHeight(x, z + 1)
    backwardHeight = mc.getHeight(x - 1, z)
    leftHeight = mc.getHeight(x, z - 1)

    if forwardHeight - currentHeight < 3:
        x += 1
        if programType == 2:
            z += 1
    elif rightHeight - currentHeight < 3:
        z += 1
        if programType == 2:
            x += 1
    elif leftHeight - currentHeight < 3:
        z -= 1
    elif backwardHeight - currentHeight < 3:
        x -= 1
    y = mc.getHeight(x, z)


pos = mc.player.getTilePos()
x = pos.x
z = pos.z
y = mc.getHeight(x, z)


while True:
    calculateMove(prType)
    mc.setBlock(x, y, z, block)
    time.sleep(sleep)
    mc.setBlock(x, y, z, 0)