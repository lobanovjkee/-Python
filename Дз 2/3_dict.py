myDict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
valuesList = sum(list(myDict.values()), [])
userInput = int(input('Введите номер месяца:'))
if userInput in valuesList:
    i = valuesList.index(userInput)
    if 0 <= i <= 2:
        print(f'{userInput}-й месяц это Зима')
    elif 3 <= i <= 5:
        print(f'{userInput}-й месяц это Весна')
    elif 6 <= i <= 8:
        print(f'{userInput}-й месяц это Лето')
    elif 9 <= i <= 11:
        print(f'{userInput}-й месяц это Осень')
else:
    print('В году только 12 месяцев попробуйте еще раз')
