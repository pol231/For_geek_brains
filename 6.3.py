class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name}, {self.surname}, {self.position}')

    def get_total_income(self):
        print(sum(self._income.values()))


worker = Position('Pavel', 'Ivanou', 'Senior', 10000, 10000)
worker.get_full_name()
worker.get_total_income()
