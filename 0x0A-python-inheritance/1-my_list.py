#!/usr/bin/python3
"""class MyList inherits from list"""


class MyList(list):
    """Function that prints the list, but sorted"""

    def print_sorted(self):
        print(sorted(self))
