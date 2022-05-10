def my_func(x, y):
    """"Возводит положительное целое число х в отрицательное число y"""
    result = x ** y
    return f'Результат возведения в степень{round(result, 4)}'
print(my_func(x=int(input('Введите первое число: ')), y=float(input('Введите второе число: '))))