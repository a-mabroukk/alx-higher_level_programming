#!/usr/bin/python3
"""function that reads a text file"""



def read_file(filename=""):
    """reads a text file"""
    with open('my_file_0.txt', 'r', encoding='UTF-8') as f:
        r_file = f.read()
        print(r_file)
