#!/usr/bin/python3
"""
    This module writes a class that
    gets it from a list.
"""


class MyList(list):
    """
        This list is supposed to only contain integers.
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
            Prints MyList lists in ascending order.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
