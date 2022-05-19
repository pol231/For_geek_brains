from itertools import cycle


с = 0
for i in cycle("ABC"):
    if с > 10:
        break
    print(i)
    с += 1
