from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(0)#задержка секунд
#координаты
valid = True

x = int(input("введите X: "))
y = int(input("введите Y: "))
z = int(input("введите Z: "))
if not -12 < x < 318:
    valid = False
if not 0 < y < 130:
    valid = False
if not 1 < z < 545:
    valid = False

if valid:
    mc.player.setTilePos(x, y, z)
    mc.postToChat("pratki nachalis!!!")

else:
    mc.postToChat("Igraem v pratki chestno! Ne teleportiruemsa daleko!")