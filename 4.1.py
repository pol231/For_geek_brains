from sys import argv
"""Считает заработную плату по формуле"""


def zp():
    try:
        vr, st, prem = map(int, argv[1:])
# vr = выработанных часов,st = ставка в час, prem = премия
        print(f'Ваша зп сосавитала - {vr*st+prem} $')
    except ValueError:
        print('Введите 3 числа')


zp()