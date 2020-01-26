from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import minecraftstuff

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
radius = 0
yplus = 0


moshnost = int(input("введите мощность бомбы 1-сильная, 2-супервынос,город-динамит,царь-бомба:    "))

if moshnost == 1:
    radius = 5
    yplus = 7
elif moshnost == 2:
    radius = 15
    yplus = 19

mcdrawing.drawSphere(pos.x, pos.y + yplus, pos.z, radius, 46)

mc.postToChat("Bomba nad vami!")
mc.postToChat("Posmotrite v konsol!")
ans = input("Если хотите взорвать бомбу нажмите тут(осторожно! взрыв гигантский(чтобы обезвредить бомбу, нажмите букву 'о'))    ")
if ans  !="о":
    time.sleep(1)
    mc.setBlock(x, y + 4, z, 152)
elif ans == "о":
    mcdrawing.drawSphere(pos.x, pos.y + yplus, pos.z, radius, 0)
    mc.postToChat("Spasibo, bomba obezvrezena!")
    print("Spasibo, bomba obezvrezena!")