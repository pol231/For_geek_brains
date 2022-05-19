def fact(n):
    num = 1
    for i in range(n + 1):
        yield (f'{i}! = {num}')
        num *= i + 1

for el in fact(int(input('Факториал числа: '))):
    print(el)