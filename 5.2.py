with open('text5_2.txt', 'r', encoding='utf-8') as data:
    my_str = data.readlines()
    for i, k in enumerate(my_str, 1):
        num = len(k.split())
        print(f'Строка {i}: {k} > содержит {num} слов ')
    print(f'Всего строк {i}')
