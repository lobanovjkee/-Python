Winter = [12, 1, 2, 'Зима']
Spring = [3, 4, 5, 'Весна']
Summer = [6, 7, 8, 'Лето']
Fall = [9, 10, 11, 'Осень']
userInput = int(input('Введите номер месяца: '))
if userInput in Winter:
    print(Winter[-1])
elif userInput in Spring:
    print(Spring[-1])
elif userInput in Summer:
    print(Summer[-1])
elif userInput in Fall:
    print(Fall[-1])
else:
    print('В году от 1 до 12 месяцев включительно, попробуйте еще раз')
