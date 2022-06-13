class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма a и b равна: ')
        return f's = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение a и b равно: ')
        return f's = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f's = {self.a} + {self.b} * i'


a = ComplexNumber(22, -56)
b = ComplexNumber(123, 78)
print(a)
print(a + b)
print(a * b)
