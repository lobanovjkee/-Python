userInput = int(input('Введите время в секундах: '))
hours = userInput // 3600
minutes = (userInput // 60) % 60
seconds = userInput % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')
