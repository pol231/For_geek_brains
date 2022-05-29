from time import sleep


class TrafficLight:
    __color = ''

    def running(self):
        print('Цвет светофора карсный')
        sleep(7)
        print('Цвет светофора желтый')
        sleep(2)
        print('Цвет светофора зеленый')
        sleep(10)


trafficlight = TrafficLight()
trafficlight.running()
