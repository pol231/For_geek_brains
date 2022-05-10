def my_sum():
    """Считает сумму введенных чисел"""
    n = 0
    while True:
        numbers = input('Введите числа через пробел, для выхода введите "q": ').split()
        for num in numbers:
            if num.lower() == 'q':
                return n
            else:
                try:
                    n += float(num)
                except ValueError:
                    print('Введите пожалуйста числа')
        print(f'Сумма числе равна: {n}')
print(my_sum())