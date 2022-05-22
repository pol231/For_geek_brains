from random import randint

with open('text5_5.txt', 'w', encoding='utf-8') as data:
    my_list = [randint(1, 100) for _ in range(100)]
    data.write(' '.join(map(str, my_list)))
print(sum(my_list))
