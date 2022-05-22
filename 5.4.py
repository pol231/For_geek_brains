my_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
with open('text5_4.txt', encoding='utf-8') as data_eng,\
         open('text5_4rus.txt', 'w+', encoding='utf-8') as data_rus:
    data_rus.writelines([i.replace(i.split()[0], my_dict.get(i.split()[0])) for i in data_eng])
