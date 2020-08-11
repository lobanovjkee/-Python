profit = int(input('Введите значение выручки компании: '))
lose = int(input('Введите значение издержек компании: '))
if profit > lose:
    efficiency = profit - lose
    print(f'Компания работает в плюс на {efficiency}.')
    print(f'Рентабельность компании {(efficiency / profit):.4f}')
    staff = int(input('Введите количество сотрудников работаюших на компанию: '))
    print(f'Прибыль на одного сотрудника состовляет {(efficiency / staff):.2f}')
else:
    print(f'Компания работает в минус на {lose - profit}.')
