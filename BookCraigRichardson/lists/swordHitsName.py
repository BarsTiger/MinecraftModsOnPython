from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    name = input("Джедай ударов по блокам правой кнопкой меча, имя свое введи...  (выйти дабы, простое слово стоп введи)  ")
    if name == "стоп":
        break
    time.sleep(0.5)
    mc.postToChat("Nachinaem! Da prebudet s vami sila!!!")

    time.sleep(15)

    blockHits = mc.events.pollBlockHits()
    blockHitsLength = len(blockHits)
    mc.postToChat("Vash chet " + str(blockHitsLength))

    scoreboard[name] = blockHitsLength


    print(scoreboard)
