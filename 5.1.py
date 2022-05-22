with open('text5_1.txt', 'w', encoding='utf-8') as data:
    while True:
        my_str = input('Введите пожалуйста данные, для окончания записи - пустую строку: ')
        if not my_str:
            break
        print(my_str, file=data)
