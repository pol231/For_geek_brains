def my_sum(n_1, n_2, n_3):
    """Показывает сумму двух наибольших чисел из трех предложенных"""
    my_list = [n_1, n_2, n_3]
    my_list.remove(min(my_list))
    return f'Ваша сумма: {sum(my_list)}'
print(my_sum(n_1=int(input("Введите первое число: ")), n_2=int(input("Введите второе число: ")), n_3=int(input("Введите третье число: "))))