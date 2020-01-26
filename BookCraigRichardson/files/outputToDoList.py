from mcpi.minecraft import Minecraft
mc = Minecraft.create()

zapominausieKotiki = open("toDoFile.txt", "r")

for zapominausiyKotik in zapominausieKotiki:
    mc.postToChat(zapominausiyKotik)
    print(zapominausiyKotik)