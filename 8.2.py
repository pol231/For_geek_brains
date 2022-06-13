class Zero:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @staticmethod
    def zero(first, second):
        try:
            return first / second
        except:
            return (f'Делить на ноль нельзя')


num = Zero(5, 0)
print(Zero.zero(5, 0))
