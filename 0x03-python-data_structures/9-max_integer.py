#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    max = my_list[0]
    for i in range(len(my_list)):
        if i > max:
            max = i
    return max
