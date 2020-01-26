# n = int(input("Введи число, до которого будут идти поколения    "))
# n = 5

def fibonacciRecAux(pokolenia, result, perv, vtor):
    if pokolenia == 1:
        return 0
    tret = perv + vtor
    # result = perv + vtor
    # pokolenia = pokolenia - 1
    if pokolenia == 0:
        return result
    else:
        return fibonacciRecAux(pokolenia - 1, result + tret, vtor, tret)


def fibonacci(n):
    return fibonacciRecAux(n, 0, 1, 0)


def fibonacciIt(pokolenia):
    if pokolenia == 1:
        return 0
    perv = 0
    vtor = 1
    result = perv + vtor
    for i in range(1, pokolenia - 1):
        tret = perv + vtor
        result = result + tret
        perv = vtor
        vtor = tret
    return result


# print(fibonacci(n, 0))
# print(fibonacciRec(n, 0, 0, 1, 0))

# res = fibonacci(n, 0)

if fibonacci(5) == 7:
    print('ok')
else:
    print('wrong for 5')

if fibonacci(6) == 12:
    print('ok')
else:
    print('wrong for 6')

if fibonacci(1) == 0:
    print('ok for 1')
else:
    print('wrong for 1')

if fibonacci(2) == 1:
    print('ok')
else:
    print('wrong for 2')

if fibonacci(3) == 2:
    print('ok')
else:
    print('wrong for 3')

if fibonacci(7) == 20:
    print('ok')
else:
    print('wrong for 7')
