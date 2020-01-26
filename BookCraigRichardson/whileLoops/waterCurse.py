from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

input("Точно? Вода потом не уйдет, а останется навсегда (если да, то нажми здесь любую клавишу)  ")

count = 0

while count < 30:
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    time.sleep(1)
    count += 1