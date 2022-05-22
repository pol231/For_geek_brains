with open('text5_3.txt', 'r', encoding='utf-8') as data:
    my_dict = {}
    for i in data:
        my_dict[i.split()[0]] = float(i.split()[1])
    print('Меньше 20000 получили: ')
for name, k in my_dict.items():
    if k < 20000:
        print(f'{name} - {k}')
print(f'Средняя зп: {sum(my_dict.values()) / 10}')