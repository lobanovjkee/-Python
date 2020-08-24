from random import randrange

my_list = [randrange(100) for el in range(0, 15)]
print(my_list)
new_list = []
for i, el in enumerate(my_list):
    if i == 0:
        pass
    elif my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
print(new_list)
