my_list = list(input('Please write anything '))
for n in range(0, len(my_list)-1, 2):
    my_list[n+1], my_list[n] = my_list[n], my_list[n+1]
print(my_list)