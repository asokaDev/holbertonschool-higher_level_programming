#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    for j in range(len(my_list)):
        div.append(0 == my_list[j] % 2)
    return div
