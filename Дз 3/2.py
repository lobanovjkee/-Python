def person_func(**person):
    for key, value in person.items():
        print(f'{key}: {value} ', end='')


person_func(name='Boris', surname="Ivanov", year_of_birth=1994, city='Moscow', email='boriska@mail.ru',
            phone='8(800)5553535')
