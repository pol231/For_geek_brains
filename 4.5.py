from functools import reduce


def my_list(prev_el, el):
    return prev_el * el


new_list = [i for i in range(100, 1001, 2)]
print(reduce(my_list, new_list))