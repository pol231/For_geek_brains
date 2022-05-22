import re

my_dict = {}

with open('text5_6.txt', 'r', encoding='utf-8') as data:
    for i in data.readlines():
        my_dict[re.findall(r'^\w+', i)[0]] = sum(map(int, re.findall(r'\d+', i)))
    print(my_dict)