class Bird(object):
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
    def birdcall(self):
        print("чик-чирик")
    def fly(self):
        print("хлоп-хлоп")
class Penguin(Bird):
    def swim(self):
        print("умеет плавать")
    def birdcall(self):
        print("квак")
    def fly(self):
        print("пингвины не летают :(")
class Parrot(Bird):
    def __init__(self, name, wingspan, color):
        self.name = name
        self.wingspan = wingspan
        self.color = color

gardenBird = Bird("Geoffrey", 12)
gardenBird.birdcall()
gardenBird.fly()
sarahThePenguin = Penguin("Sarah", 10)
sarahThePenguin.swim()
sarahThePenguin.fly()
sarahThePenguin.birdcall()
freddieTheParrot = Parrot("Freddie", 12, "синий")

print(freddieTheParrot.color)
freddieTheParrot.fly()
freddieTheParrot.birdcall()