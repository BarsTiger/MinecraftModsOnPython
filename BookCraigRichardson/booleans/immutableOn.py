from mcpi.minecraft import Minecraft
mc = Minecraft.create()

immutableIs = False

mc.setting("world_immutable", immutableIs)