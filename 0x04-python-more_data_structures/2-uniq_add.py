#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    my_list.sort()
    if my_list is not None or my_list is not []:
        add += my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] is not my_list[i - 1]:
            add += my_list[i]
    return add
