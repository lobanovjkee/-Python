with open('text_2.txt', 'r', encoding='UTF-8') as text_2:
    context = text_2.readlines()
    i = 1
    strings = len(context)
    print(f'В данном файле {strings} строки')
    for word in context:
        print(f'В {i} строке {len(word.split())} слов')
        i += 1
