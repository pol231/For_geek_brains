my_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
my_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']

user = int(input('Please enter any number month'))
if user in sum(my_dict.values(), []):
    for i in my_dict.items():
        if user in i[1]:
            print(f'{user} month is {i[0]}')
            break
print(f'{user} month is {my_list[user - 1]}')