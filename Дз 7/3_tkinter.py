from tkinter import *


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

    def make_order(self, digit, x1, y1, x2, y2):
        while self.cells > 0:
            digit = digit if digit < self.cells else self.cells
            self.cells -= digit
            for i in range(digit):
                canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y1, x1, y1)
                x1 += 15
                x2 += 15
            x1 = x1 - (15 * digit)
            x2 = x2 - (15 * digit)
            y1 += 15
            y2 += 15


root = Tk()


def on_click():
    Label(root, text='Сложение').place(x=10, y=270)
    Label(root, text='Вычитание').place(x=310, y=270)
    Label(root, text='Умножение').place(x=10, y=570)
    Label(root, text='Деление').place(x=310, y=570)

    input_1.place_forget()
    input_2.place_forget()
    input_3.place_forget()
    button.place_forget()
    try:
        cell_1 = Cell(int(input_1.get()))
        cell_2 = Cell(int(input_2.get()))

        cell_3 = Cell(cell_1 + cell_2)
        cell_4 = Cell(cell_1 - cell_2)
        cell_5 = Cell(cell_1 * cell_2)
        cell_6 = Cell(cell_1 / cell_2)
        cell_3.make_order(int(input_3.get()), 10, 10, 20, 20)
        cell_4.make_order(int(input_3.get()), 310, 10, 320, 20)
        cell_5.make_order(int(input_3.get()), 10, 310, 20, 320)
        cell_6.make_order(int(input_3.get()), 310, 310, 320, 320)
    except ValueError:
        Label(root, text='Ошибка введите только числа!').place(x=185, y=10)


canvas = Canvas(root, width=600, height=600, bg='white')
canvas.grid(column=0, row=0)

input_1 = Entry(root, bg='grey', width=37)
input_2 = Entry(root, bg='grey', width=37)
input_3 = Entry(root, bg='grey', width=37)
input_1.place(x=150, y=150)
input_2.place(x=150, y=200)
input_3.place(x=150, y=250)
input_1.insert(0, 'Cell 1')
input_2.insert(0, 'Cell 2')
input_3.insert(0, 'Количество ячеек в ряду')

button = Button(root, width=5, bg='grey', text='Start', command=on_click)
button.place(x=380, y=300)
canvas.create_line(0, 300, 600, 300)
canvas.create_line(300, 0, 300, 600)

root.mainloop()
