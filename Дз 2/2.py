newList = input('Введите элементы списка через пробел: ').split(' ')
print(newList)
j = 0
for i in newList:
    while j < len(newList):
        if (len(newList) % 2) != 0 and j == (len(newList) - 1):
            break
        else:
            newList[j], newList[j + 1] = newList[j + 1], newList[j]
            j += 2
print(newList)
