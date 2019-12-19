#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = list(a_dictionary)
    key.sort()
    for i in range(len(key)):
        print("{}: {}".format(key[i], a_dictionary[key[i]]))
