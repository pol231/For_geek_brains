my_list = [9, 8, 8, 7, 7, 7, 6, 5, 4, 4, 3, 2, 2, 2, 1, 1]
new_number = ''
while new_number != 'q':
    i = 0
    new_number = input('Please enter any digit. To escape please enter - q :')
    if new_number.isdigit():
        for n in my_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(new_number))
    print(my_list)