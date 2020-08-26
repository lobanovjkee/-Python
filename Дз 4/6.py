from itertools import cycle, count

count_list = []
cycle_list = []
user_input = int(input('Введите число с которого начнется итерация: '))
for el in count(user_input):
    if len(count_list) > 15:
        break
    else:
        count_list.append(el)
print(count_list)
for el in cycle(count_list):
    if len(cycle_list) > len(count_list) * 3:
        break
    else:
        cycle_list.append(el)
print(cycle_list)
