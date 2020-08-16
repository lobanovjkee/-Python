goods = []
i = 1
userInput = ''
while userInput != 'нет'.lower():
    userInput = input('Для просмотра аналитики введите нет, для продолжения ввода нажмите Enter: ').lower()
    if userInput == 'Нет'.lower():
        break
    else:
        order = [i]
        newGood = {'Название': input('Введите название: '), 'Цена': input('Введите цену: '),
                   'Количество': input('Введите количество: '), 'Ед.': input('Введите единицу измерения: ')}
        order.append(newGood)
        order = tuple(order)
        goods.append(order)
        i += 1
        print(goods)
newGoods = []
for i in goods:
    newGoods.append(list(i[1].values()))
goods = {'Название': [], 'Цена': [], 'Количество': [], 'Ед.': []}
for i in newGoods:
    goods['Название'].append(i[0])
    goods['Цена'].append(i[1])
    goods['Количество'].append(i[2])
    goods['Ед.'].append(i[3])
print(
    f'\n "Название": {goods["Название"]} \n "Цена": {goods["Цена"]}'
    f'\n "Количество": {goods["Количество"]} \n "Ед.": {set(goods["Ед."])}')
