class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            self.is_police = 'Это полицейская машина'
        else:
            self.is_police = 'Это не полицейская машина'

    def go(self):
        print(f'{self.name} поехала вперед')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        user_input = input('Введите направление: ')
        if user_input == 'left':
            print(f'{self.name} повернула налево')
        elif user_input == 'straight':
            print(f'{self.name} едет прямо')
        elif user_input == 'right':
            print(f'{self.name} повернула направо')
        elif user_input == 'back':
            print(f'{self.name} повернула назад')

    def show_speed(self):
        print(f'{self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if int(self.speed) > 60:
            print('Скорость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if int(self.speed) > 40:
            print('Скорость превышена!')


class PoliceCar(Car):
    pass


town_car = TownCar(55, 'зеленый', 'TownCar', False)
sport_car = SportCar(210, 'красный', 'SportCar', False)
work_car = WorkCar(43, 'желтый', 'WorkCar', False)
police_car = PoliceCar(70, 'черно-белый', 'PoliceCar', True)

town_car.go()
print(f'{town_car.is_police}, цвета: {town_car.color}')
town_car.show_speed()
town_car.turn()
town_car.stop()
print(30 * '*')

sport_car.go()
print(f'{sport_car.is_police}, цвета: {sport_car.color}')
sport_car.show_speed()
sport_car.turn()
sport_car.stop()
print(30 * '*')

work_car.go()
print(f'{work_car.is_police}, цвета: {work_car.color}')
work_car.show_speed()
work_car.turn()
work_car.stop()
print(30 * '*')

police_car.go()
print(f'{police_car.is_police}, цвета: {police_car.color}')
police_car.show_speed()
police_car.turn()
police_car.stop()
