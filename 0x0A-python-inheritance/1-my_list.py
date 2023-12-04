#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """constructor"""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
