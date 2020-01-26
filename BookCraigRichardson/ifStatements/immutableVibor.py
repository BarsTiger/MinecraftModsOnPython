from mcpi.minecraft import Minecraft
mc = Minecraft.create()

answer = input("Защитить мир от изменений? Д/Н")
if answer == "д":
    mc.setting("world_immutable", True)
    mc.postToChat("Zashita vkl")

else:
    mc.setting("world_immutable", False)
    mc.postToChat("Zashita vikl")