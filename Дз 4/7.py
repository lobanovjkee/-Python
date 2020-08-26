def fact(n):
    for elm in range(1, n + 1):
        yield elm


f = 1
user_input = int(input('Введите число, чтобы узнать его факториал: '))
for el in fact(user_input):
    f *= el
print(f'{user_input}! = {f}')
