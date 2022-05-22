import json

with open('text5_7.json', 'w', encoding='utf-8') as data_write, \
        open('text5_7.txt', 'r', encoding='utf-8') as data_reed:
    earn = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in data_reed}
    lose = [i for i in earn.values() if i > 0]
    mid = [earn, {'Средняя прибыль ': sum(lose) / 4}]
    print(lose)
    print(mid)

    json.dump(mid, data_write, ensure_ascii=False)
