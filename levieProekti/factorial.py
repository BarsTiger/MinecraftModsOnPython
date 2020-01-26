n = int(input("Введи число, до которого будет факториал    "))


def factorial(kolvo):
    fakt = 1
    for i in range(1, kolvo + 1):
        fakt = fakt * i
    return fakt


def factTailRec(kolvo, result):
    if kolvo == 0:
        return result
    else:
        return factTailRec(kolvo - 1, result * kolvo)


def fact(kolvo):
    if kolvo == 1:
        return 1
    else:
        return kolvo * fact(kolvo - 1)



print(factorial(n))
print(factTailRec(n, 1))
print(fact(n))

if factorial(n) == factTailRec(n, 1) and factorial(n) == fact(n):
    print("all OK")

schislo = factorial(n)

print( "dlina " + str(len(str(schislo))) + " simvola")