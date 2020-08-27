with open('text_1.txt', 'x+', encoding='UTF-8') as text_1:
    magic = True
    while magic is True:
        user_input = input()
        if user_input == '':
            magic = False
        else:
            print(user_input, file=text_1)
