#Задание 2.

from random import randint

#O(n^2)
def list_min_n2(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i

#O(n)
def list_min_n(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value

lst1 = [randint(0,100) for i in range(20)]
print(lst1)
print(list_min_n2(lst1))
print(list_min_n(lst1))