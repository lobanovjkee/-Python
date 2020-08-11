userInput = input('Введите число: ')
if int(userInput) < 0:
    print('Ошибка попробуйте еще раз.')
else:
    a = userInput
    b = 2 * userInput
    c = 3 * userInput
    print(int(a) + int(b) + int(c))
