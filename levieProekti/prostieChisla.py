n = int(input("Введи число, до которого я найду простые числа:     "))

def finder(n):
    prostie = []
    ost = 0
    for i in range(n):
        ost = i % range(i)