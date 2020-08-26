from random import randrange

my_list = [randrange(100) for el in range(15)]
new_list = []
print(my_list)
for i, el in enumerate(my_list):
    if my_list.count(my_list[i]) > 1:
        pass
    else:
        new_list.append(my_list[i])
print(new_list)
