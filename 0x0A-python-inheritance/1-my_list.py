#!/usr/bin/python3
"""This module contain the sort function for a list"""


class MyList(list):
    def __init__(self):
        """Constructor"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
