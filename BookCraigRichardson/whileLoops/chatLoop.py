from mcpi.minecraft import Minecraft
mc = Minecraft.create()

user = input('Введите имя на английском:  ')

while True:
    soobsh = input('Введите сообщение(vot takimi bukvami)(чтобы закончить чат, введите stop):  ')
    if soobsh == 'stop':
        break
    else:
        mc.postToChat(user + ': ' + soobsh)
