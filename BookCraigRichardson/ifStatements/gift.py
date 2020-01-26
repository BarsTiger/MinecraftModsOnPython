from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 91
y = 77
z = 341
gift = mc.getBlock(x, y, z)

if gift == 57:
    mc.postToChat("Bog almazov ochen rad!")
    time.sleep(3)
    mc.setBlock(x, y, z, 0)

elif gift == 103:
    mc.postToChat("Arbuz - toze normalno")
    time.sleep(3)
    mc.setBlock(x, y, z, 0)
else:
    mc.player.setTilePos(100.859, 64, 357.531)
    mc.postToChat("Nuzno davat podarki! Postav almazniy blok na arbuz i nazmi (Sm python console)!")
    mc.setBlock(x, y, z, 0)
    input("Нажми любую клавишу")
    if mc.getBlock(101, 64,  357) == 57:
        mc.setBlock(101,64 ,357 , 0)
        mc.player.setPos(94, 76, 341)
        mc.postToChat("Spasibo")


