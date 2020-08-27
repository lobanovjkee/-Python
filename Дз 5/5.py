with open('text_5.txt', 'w', encoding='UTF-8') as text_5:
    user_input = input('Введите числа через пробел чтобы узнать их сумму: ')
    print(user_input, file=text_5)

with open('text_5.txt', 'r', encoding='UTF-8') as text_5:
    context = text_5.read().split()
    try:
        context = [int(item) for item in context]
        print(sum(context))
    except ValueError:
        print('Введите только числа')
