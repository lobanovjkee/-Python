myList = input('Введите какое-то количество слов через пробел: ').split(' ')
j = 1
for i in myList:
    print(f'{j} - {i[:10]}')
    j += 1
