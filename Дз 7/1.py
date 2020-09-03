class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end='    ')
            print()
        return ''

    def __add__(self, other):
        try:
            if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
                result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                          for i in range(len(self.matrix))]
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        print(result[i][j], end='    ')
                    print()
                return ''
        except IndexError:
            return 'Матрицы не равны, сложение не возможно'


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m_1)
m_2 = Matrix([[2, 2, 2], [1, 1, 1], [3, 3, 3]])
print(m_2)
print(m_1 + m_2)
