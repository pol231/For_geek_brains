class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self, weight=25, sloi=5):
        self.weight = weight
        self.sloi = sloi
        print(f'{self._lenght*self._width*self.weight*self.sloi /  1000} тонн')


road = Road(20, 5000)
road.mass()
