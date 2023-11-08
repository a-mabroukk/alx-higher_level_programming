#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_add = set(my_list)
    for i in uniq_add:
        sum += i
    return sum
