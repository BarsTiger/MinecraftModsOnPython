class Cat(object):

    owner = "Андрей"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getWeightInGrams(self):
        return self.weight * 1000

    def eat(self, food):
        self.weight = self.weight + 0.05
        print(self.name + " ест " + food)

    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " теперь спит...")

myCat = Cat("Барсик", 4.5)
mySecondCat = Cat("Мурка", 3.9)
mySecondCat.owner = "Бабу:)"
print("имя кота: " + str(myCat.name))
print("имя кошки: " + str(mySecondCat.name))
print("вес кота до еды: " + str(myCat.weight))
print("вес кота до еды в граммах: " + str(myCat.getWeightInGrams()))
mySecondCat.eat("торт")
myCat.eatAndSleep("рыбу")

print("вес кота после еды: " + str(myCat.weight))
print("вес котапосле еды в граммах: " + str(myCat.getWeightInGrams()))

print(myCat.owner)
print(mySecondCat.owner)