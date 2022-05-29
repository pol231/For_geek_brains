class Stationery:
    def __init__(self, title='рисуем кистью'):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки: {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'запуск отрисовки: рисуем ручкой {self.title} ')


class Pencil(Stationery):
    def draw(self):
        print(f'запуск отрисовки: риуем карандашами {self.title} ')


class Handle(Stationery):
    def draw(self):
        print(f'запуск отрисовки: риуем маркером {self.title} ')


stationery = Stationery()
pen = Pen('Berlingo')
pencil = Pencil('Easy kids')
handle = Handle('Uni pin')

my_list = [stationery, pen, pencil, handle]

for i in my_list:
    i.draw()
    print()
