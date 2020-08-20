def my_func(v_1, v_2):
    try:
        print(v_1 / v_2)
    except ZeroDivisionError:
        print('На ноль делить нельзя, попробуйте заново')


print('Введите числа которые хотите разделить')
v1 = int(input())
v2 = int(input())
my_func(v1, v2)
