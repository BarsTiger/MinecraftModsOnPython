from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103

def water():
    return 9

def dinamit():
    return 46

def fakel():
    return 50

def dragonEgg():
    return 122

def maak():
    return 138

def morskoyfonar():
    return 169

def ogon():
    return 51

def almazniyBlock():
    return 57


def voproshalka():
    polzovatelZabilIDBloka = input("Введите название блока:   ")
    if polzovatelZabilIDBloka == "арбуз":
        return melon()
    elif polzovatelZabilIDBloka == "вода":
        return water()
    elif polzovatelZabilIDBloka == "динамит":
        return dinamit()
    elif polzovatelZabilIDBloka == "факел":
        return fakel()
    elif polzovatelZabilIDBloka == "драконье яйцо":
        return dragonEgg()
    elif polzovatelZabilIDBloka == "маяк":
        return maak()
    elif polzovatelZabilIDBloka == "морской фонарь":
        return morskoyfonar()
    elif polzovatelZabilIDBloka == "огонь":
        return ogon()
    elif polzovatelZabilIDBloka == "алмазный блок":
        return almazniyBlock()


def stavilka():
    block = voproshalka()
    mc.postToChat(block)
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos. y, pos.z, block)


stavilka()
