from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(0)#задержка секунд
#координаты
x = int(input("введите X: "))
y = int(input("введите Y: "))
z = int(input("введите Z: "))
mc.player.setTilePos(x, y, z)