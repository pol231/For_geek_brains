class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:01}" for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            mat = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                for line in range(len(self.data))]
            return Matrix(mat)
        except IndexError:
            return f'Не соответствие размерам матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]
mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2
print()
print(new_m)
