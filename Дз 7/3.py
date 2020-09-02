class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        return abs(self.cells - other.cells)

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        if self.cells > other.cells:
            return int(self.cells / other.cells)
        else:
            return int(other.cells / self.cells)

    def make_order(self, digit):
        while self.cells > 0:
            digit = digit if digit < self.cells else self.cells
            self.cells -= digit
            print('❤ ' * digit)


cell_1 = Cell(12)
cell_2 = Cell(3)

cell_3 = Cell(cell_1 + cell_2)
print(cell_3.cells)
cell_3.make_order(10)
print('_' * 30)

cell_3 = Cell(cell_1 - cell_2)
print(cell_3.cells)
cell_3.make_order(10)
print('_' * 30)

cell_3 = Cell(cell_1 * cell_2)
print(cell_3.cells)
cell_3.make_order(10)
print('_' * 30)

cell_3 = Cell(cell_1 / cell_2)
print(cell_3.cells)
cell_3.make_order(10)
print('_' * 30)
