userInput = int(input('Введите целое положительное число: '))
defMax = 0
while userInput > 0:
    newMax = userInput % 10
    userInput = userInput // 10
    if defMax <= newMax:
        defMax = newMax
    else:
        defMax = defMax
print(defMax)
