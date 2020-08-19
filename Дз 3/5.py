def my_func(z):
    return sum(z)


sum_list = []
magic = True
while magic is True:
    userInput = input('Введите числа через пробел, для подсчета их суммы, чтобы выйти из программы нажмите q: ')
    sum_list = sum_list + userInput.split()
    for i, el in enumerate(sum_list):
        if sum_list[i].isdigit():
            sum_list[i] = int(el)
        elif sum_list[i] == 'q':
            sum_list.remove('q')
            magic = False
    x = my_func(sum_list)
    print(x)
    sum_list = [str(x)]
