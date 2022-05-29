from random import choice


class Car:

    napr = ['направо', 'налево']

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'машина:{name} цвета {color}. Это полциейская машина? {is_police}')

    def go(self):
        print(f'{self.name}: машина поехала')

    def stop(self):
        print(f'{self.name}: машина остановилась')

    def turn(self):
        print(f'{self.name}: машина свернула {choice(self.napr)} ')

    def show_speed(self):
        print(f'{self.name}: машина едет со скоростью:{self.speed}')


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: машина едет со скоростью:{self.speed}. Превышение' if self.speed > 60 else super.show_speed()


class SportCar(Car):

    def show_speed(self):
        return f'{self.name}: машина едет со скоростью:{self.speed}. Превышение' if self.speed > 40 else super.show_speed()


class WorkCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)


town_car = TownCar('Mersedez', 'black', 100)
sport_car = SportCar('F1', 'Red', 80)
work_car = WorkCar('Газель', 'белый', 60)
police_car = PoliceCar('Mazda', 'blue', 80)
print()
town_car.turn()
sport_car.go()
work_car.stop()
print()

my_list = [town_car, sport_car, work_car, police_car]

for i in my_list:
    print(i.show_speed())
    print()
