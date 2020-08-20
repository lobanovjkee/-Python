def my_func(v_1, v_2, v_3):
    new_list = [v_1, v_2, v_3]
    new_list.remove(min(new_list))
    print(sum(new_list))


v1 = int(input())
v2 = int(input())
v3 = int(input())
my_func(v1, v2, v3)
