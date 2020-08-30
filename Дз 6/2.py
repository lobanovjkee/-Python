class Road:
    const_mass = 25

    def __init__(self, _length, _width, _height):
        self.length = _length
        self.width = _width
        self._height = _height

    def calc(self):
        mass = float(self.length) * float(self.width) * Road.const_mass * float(self._height)
        print(f'{self.length}м * {self.width}м * {Road.const_mass}кг * {self._height}см = {int(mass / 1000)}Т')


def road_calc():
    try:
        user_length = input('Введите длину дороги: ')
        user_width = input('Введите ширину дороги: ')
        user_height = input('Введите высоту дороги: ')
        road = Road(user_length, user_width, user_height)
        road.calc()
    except ValueError:
        print('Ошибка введите числа!')


user_input = ''
while user_input != 'q':
    road_calc()
    user_input = input('Если хотите продолжить нажмите Enter, для выхода введите "q": ')
