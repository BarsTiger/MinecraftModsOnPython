from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(15)

blockHits = mc.events.pollBlockHits()
blockHitsLength = len(blockHits)
mc.postToChat("Vash chet " + str(blockHitsLength))
