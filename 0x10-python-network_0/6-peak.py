#!/usr/bin/python3
def find_peak(list_of_integers):
    i = 1
    if (not list_of_integers):
        return None
    if (list_of_integers[0] >= list_of_integers[2]):
        return list_of_integers[0]
    if (len(list_of_integers) - 1 >= len(list_of_integers) - 2):
        return len(list_of_integers) - 1
    # check for every other element
    for i in range(len(list_of_integers), len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
