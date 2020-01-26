from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Location(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

bedroom = Location(96, 80, 341)
mc.player.setTilePos(bedroom.x, bedroom.y, bedroom.z)