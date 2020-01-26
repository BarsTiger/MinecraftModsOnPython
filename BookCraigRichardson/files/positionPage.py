from flask import Flask
app = Flask(__name__)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = str(pos.x), str(pos.y), str(pos.z)

@app.route("/")
def showPosition():
    return "Ваши координаты на момент запуска программы: " + "х-" + x + ", y-" + y + ", z-" + z
app.run()