class Error:
    def __init__(self, my_list):
        self.my_list = []

    def my_num(self):

        while True:
            try:
                val = int(input('Введите целые числа: '))
                self.my_list.append(val)
                print(f'{self.my_list}\n')
            except:
                print(f"Вводите только целые чила")
                esc = input(f'Продолжить ввод?: Y/N ')

                if esc == 'Y':
                    print(try_except.my_num())
                elif esc == 'N':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_num())
