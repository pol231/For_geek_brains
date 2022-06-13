class Orgtehnica:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель ': self.name, 'Цена ': self.price, 'Количество ': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель ': unit, 'Цена ': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Введенные данные -\n {self.my_store}')
        except:
            return f'Неверные данные'


class Printer(Orgtehnica):
    def print(self):
        return f'to print smth {self.numb} times'


class Scanner(Orgtehnica):
    def scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Orgtehnica):
    def copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp laserJet', 2015, 10, 5)
unit_2 = Scanner('Samsung', 2000, 4, 5)
unit_3 = Copier('Microsoft', 4000, 8, 5)
print(unit_1.reception())
