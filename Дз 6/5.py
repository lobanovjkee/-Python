class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} нарисовала круг ◯')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} нарисовал квадрат ☐')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} нарисовал треугольник △')


pen = Pen('ручка')
pencil = Pencil('карандаш')
marker = Handle('маркер')
pen.draw()
pencil.draw()
marker.draw()
