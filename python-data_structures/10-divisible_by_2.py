#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for i in my_list:
        if i % 2 == 0:
            i = True
        else:
            i = False
        list_result.append(i)
    return list_result
