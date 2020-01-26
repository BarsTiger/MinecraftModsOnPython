from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"основной дом": (95, 76, 341), "пристройка": (94, 75, 352), "сундучная": (70, 64, 361), "библиотека": (81, 69, 352), "дом отдыха": (104, 82, 324), "поляна": (-32, 64, -197), "горный дом": (68, 89, 351), "дом на дереве": (-439, 66, 2212)}

choice = ""

while choice != "стоп":
    choice = input("Введите название комнаты вашего дома, или стоп, для выхода  ")

    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]

        mc.player.setPos(x, y, z)
    elif choice != "стоп" and choice not in places:
        print("Но такой комнаты, как ни странно, нет в вашем гигантском доме :(")