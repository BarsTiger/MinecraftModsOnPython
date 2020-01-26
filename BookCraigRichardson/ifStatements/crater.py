from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Точно создать кратер? Он может уничтожить находящиеся рядом постройки! Д/Н")

if answer == "Д" or answer == "д" :

    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
    mc.postToChat("Babah!!!")