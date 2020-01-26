from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(20)#задержка секунд
#координаты
x = 57
y = 100
z = 31
mc.player.setTilePos(x, y, z)
time.sleep(20)#задержка секунд
x = 158
y = 1000
z = 154
mc.player.setTilePos(x, y, z)