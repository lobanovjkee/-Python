start = int(input('Введите начальное количество километров: '))
end = int(input('Введите желаемое количество километров: '))
days = 1
if (start or end) < 0:
    print('Ошибка попробуйте заново')
elif start > end:
    print('Ошибка попробуйте заново')
elif start == 0:
    print('Ошибка попробуйте заново')
else:
    while start < end:
        start = start + start * 0.1
        days += 1
    print(days)
