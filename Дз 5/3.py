with open('text_3.txt', 'r', encoding='UTF-8') as text_3:
    context = text_3.readlines()
    idk = []
    last_names = []
    salary = []
    salary_cap = 20000
    for word in context:
        idk.append(word.split())
    new_context = dict(idk)
    for i in new_context:
        if float(new_context[i]) < salary_cap:
            last_names.append(i)
    for j in new_context:
        salary.append(float(new_context[j]))
    print(
        f'Сотрудники с зарплатой меньше {salary_cap}: {last_names} '
        f'\nСредний доход сотрудников {sum(salary) / len(salary)}')
