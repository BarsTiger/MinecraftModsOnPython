from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

input("Здравствуйте! Вы выбрали нашу фирму по телепортационным турам в Майнкрафте. Пожалуйста, если вы готовы нажмине клавишу здесь  ")

mc.player.setTilePos(68, 87, 334)
mc.postToChat("Pozaluysta, oplatite tour almaznim blokom postavlennim na steklo")
input("Поставьте блок и нажмите здесь    ")

#основа, телепортирует игрока, пишет месседж, и ждет заданное кол-во секунд
def teleport(x, y, z, message, sleep):
    mc.player.setTilePos(x, y, z)
    mc.postToChat(message)
    time.sleep(sleep)


if mc.getBlock(69, 87, 332) == 57:
    input("Начинаем тур! Нажмите клавишу здесь ")
    mc.setBlock(69, 87, 332, 0)

    time.sleep(1)

    teleport(46, 152, 302, "pravda krasivo? seychas mi poedem tuda", 20)
    teleport(47, 90, 289, "pogulayte tut", 40)

    mc.postToChat("obratite vnimanie na sliz. eto batut")

    teleport(9, 107, 272, "pogulayte vozle taynika", 30)
    teleport(8, 105, 280, "mi seycas v taynike. proydite v pesseru", 20)
    teleport(8, 105, 280, "mozete viprignut na batut", 15)
    teleport(-59, 97, 307, "pravda krasivo? seychas mi poedem tuda", 20)
    teleport(-58, 76, 292, "pogulayte tut", 40)
    teleport(-37, 77, 311, "", 20)
    teleport(-121, 140, 268, "ochen krasivoe mesto", 50)
    teleport(-40, 78, 256, "posmotrite naverh", 20)

    mc.postToChat("mozete idti v peseru")
    time.sleep(20)

    teleport(-95, 81, 298, "", 15)
    teleport(-80, 73, 295, "", 60)
    teleport(121, 140, 268, "pravda krasivo? no mi tuda ne edem. s zemli vid ne ochen", 30)
    teleport(-388, 42, 788, "a eto zabrosennaa sahta. mi gulaem tut dolgo. nikuda ne upadite", 80)
    teleport(999, 103, 1016, "kruto?", 80)
    teleport(1017, 126, 1024, "super", 60)
    teleport(1062, 113, 1027, "ozertso", 30)
    teleport(1136, 89, 1008, "i pustina radom", 50)
    teleport(1283, 76, 841, "taiga", 80)
    teleport(1358, 66, 1054, "savanna", 80)
    teleport(1393, 69, 1260, "krasivaa derevna", 80)

    mc.player.setTilePos(68, 87, 334)
    mc.postToChat("spasibo za polzovanie")