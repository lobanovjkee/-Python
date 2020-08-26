from sys import argv

script_name, hours_worked, salary_rate, bonus = argv

try:
    print(f'Зарплата составит {(int(hours_worked) * int(salary_rate)) + int(bonus)}')
except ValueError:
    print('Ошибка')
