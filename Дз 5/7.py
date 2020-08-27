import json

with open('text_7.txt', 'r', encoding='UTF-8') as text_7:
    context = text_7.readlines()
    firm_and_profit = []
    final = []
    counter = 0
    average_profit = {'average_profit': 0}
    for word in context:
        i = 0
        temp_list = word.split()
        temp_list[2], temp_list[3] = int(temp_list[2]), int(temp_list[3])
        temp_list.append(temp_list[2] - temp_list[3])
        while i < 3:
            temp_list.remove(temp_list[1])
            i += 1
        firm_and_profit.append(temp_list)
    firm_and_profit = dict(firm_and_profit)
    for i in firm_and_profit.values():
        if i > 0:
            average_profit['average_profit'] += i
            counter += 1
    average_profit['average_profit'] = average_profit.get('average_profit') / counter
    final.append(firm_and_profit)
    final.append(average_profit)

with open('text_7.json', 'w', encoding='UTF-8') as text_7j:
    json.dump(final, text_7j, ensure_ascii=False, indent=2)
