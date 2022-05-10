def my_func(n_1, n_2):
    """"Выполняет деление двух чисел"""
    try:
        n_1, n_2 = int(n_1), int(n_2)
        div = n_1 // n_2
    except (ValueError, ZeroDivisionError):
        return ' Введены не коректные данные'
    return div
print(my_func(input('Введите первое число: '), input('Введите второе число: ')))