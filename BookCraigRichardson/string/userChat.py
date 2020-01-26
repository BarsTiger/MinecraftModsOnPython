from mcpi.minecraft import Minecraft
mc = Minecraft.create()
user = input('Введите имя на английском:  ')
soobsh = input('Введите сообщение:  ')
mc.postToChat(user + ': ' + soobsh)
