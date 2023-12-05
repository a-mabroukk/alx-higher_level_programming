#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, 'w', encoding='UTF-8') as f:
        w_file = f.write(text)
        return w_file
