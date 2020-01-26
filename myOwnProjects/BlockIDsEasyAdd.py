from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import shelve

blockIDs = shelve.open("idsFile.db")

ans = input("Введи название блока или букву 'д', чтобы добавить блокТайп:   ")

if ans != "д":
    if ans in blockIDs:
        print(blockIDs[ans])
    elif ans not in blockIDs:
        print("Вы еще не добавили блока с таким названием :(")

elif ans == "д":
    nameOfBlock = input("Введите название блока, который хотите добавить:  ")
    blockNumber = input("Введите номер этого блока:   ")

    blockIDs[nameOfBlock] = blockNumber
    blockIDs.close()