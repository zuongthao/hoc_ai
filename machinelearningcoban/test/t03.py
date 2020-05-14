def list_doubler(lst):
    doubled = []
    for num in lst:
        doubled.append(num*2)
    return doubled
my_list = [21, 2, 93]
print(list_doubler(my_list))

doubled = [num * 3 for num in my_list]
print(doubled)