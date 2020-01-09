#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    cont = 0
    try:
        for elem in range(0, x):
            print(my_list[elem], end="")
            cont += 1
        print()
        return cont
    except IndexError:
        print()
        return cont
