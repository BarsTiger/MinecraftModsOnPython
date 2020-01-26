from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
block = 35

def getWoolState(color):
    if color == "розовый":
        blockState = 6
    elif color == "бирюзовый":
        blockState = 9
    elif color == "голубой":
        blockState = 3
    elif color == "желтый":
        blockState = 4
    elif color == "зеленый":
        blockState = 13
    elif color == "коричневый":
        blockState = 12
    elif color == "красный":
        blockState = 14
    elif color == "оранжевый":
        blockState = 1
    elif color == "зеленый":
        blockState = 5
    elif color == "светло-серый":
        blockState = 8
    elif color == "серый":
        blockState = 7
    elif color == "синий":
        blockState = 11
    elif color == "черный":
        blockState = 15
    elif color == "белый":
        blockState = 0
    return blockState

colorString = input("Введите цвет блока:  ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.postToChat("Tip i cvet blocka: " + str(block) + "," + str(state))
mc.setBlock(pos.x, pos.y, pos.z, block, state)
