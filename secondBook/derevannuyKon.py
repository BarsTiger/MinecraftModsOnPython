from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block
import minecraftstuff as minecraftstuff
import time

horseBlocks = [
minecraftstuff.ShapeBlock(0,0,0,block.WOOD_PLANKS.id),
minecraftstuff.ShapeBlock(-1,0,0,block.WOOD_PLANKS.id),
minecraftstuff.ShapeBlock(1,0,0,block.WOOD_PLANKS.id),
minecraftstuff.ShapeBlock(-1,-1,0,block.WOOD_PLANKS.id),
minecraftstuff.ShapeBlock(1,-1,0,block . WOOD_PLANKS.id),
minecraftstuff.ShapeBlock(1,1,0,block.WOOD_PLANKS.id),
minecraftstuff.ShapeBlock(2,1,0,block.WOOD_PLANKS.id)]

horsePos = mc.player.getTilePos()
horsePos.z = horsePos.z + 1
horsePos.y = horsePos.y + 1

horseShape = minecraftstuff.MinecraftShape(mc,horsePos,horseBlocks)

for count in range(1,10):
    horseShape = minecraftstuff.MinecraftShape(mc, horsePos, horseBlocks)
    time.sleep(1)
    horseShape.moveBy(1,0,0)
    horseShape.clear()