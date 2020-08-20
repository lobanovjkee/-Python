def my_func_ez(x, y):
    if y < 0:
        print(x ** y)
    else:
        print('Ошибка')


def my_func_hard(x, y):
    if y < 0:
        i = 1
        new_x = x
        while i < abs(y):
            new_x *= x
            i += 1
        print(1 / new_x)
    else:
        print('Ошибка')


v1 = int(input())
v2 = int(input())
my_func_ez(v1, v2)
my_func_hard(v1, v2)
