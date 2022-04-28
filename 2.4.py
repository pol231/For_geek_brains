my_str = input('Please enter any word without space ').split()
for n, word in enumerate(my_str, 1):
    print(f'{n}) {word[:10]}')