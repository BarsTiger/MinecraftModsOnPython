from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import shelve

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    structure = []

    print("Подождите, пока мы смотрим видео про котиков и заставляем себя начать копировать блоки воздуха, которые вы случайно добавили в пространство копирования, в список")
    print("ЧТО? Так быстро закончилось видео? Ну ладно, начинаем. А вы пока покормите своих оцелотов")

    for row in range(height):
        structure.append([])
        for column in range(width):
            structure[row].append([])
            for depth in range(length):
                block = mc.getBlock(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)
    return structure


input("Подойдите к одному углу констукции и нажмите  ")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Подойдите к противоположному углу и нажмите   ")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

structure = copyStructure(x1, y1, z1, x2, y2, z2)

structureName = input("Как назовем конструкцию?   ")

superBuildsFile = shelve.open("superBuildsFile.db")
superBuildsFile[structureName] = structure
superBuildsFile.close()

