class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        total_income = self.income['wage'] + self.income['bonus']
        print(total_income)


worker_1 = Position('Vitya', 'Ivanov', 'pro', 12, 23)
worker_1.get_full_name()
print(worker_1.position)
worker_1.get_total_income()

worker_2 = Position('Vova', 'Petrov', 'Teacher', 10, 200)
worker_2.get_full_name()
print(worker_2.position)
worker_2.get_total_income()
