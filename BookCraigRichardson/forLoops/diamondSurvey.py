from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

podnozniyBlock = mc.getBlock(x, y, z)
blockPodNogami = []

for item in range(80):
    blockPodNogami.append(podnozniyBlock)
    y = y - 1
    podnozniyBlock = mc.getBlock(x, y, z)
    if 56 in blockPodNogami:
        mc.postToChat("Almazi na pribliz. glubine " + str(blockPodNogami.index(56)))
        break
    else:
        mc.postToChat("Rudi net :(")

print(blockPodNogami)




