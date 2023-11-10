#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    devi = 0
    floated = 0
    if my_list == "":
        return 0
    for int_num in my_list:
        average += int_num[0] * int_num[1]
        devi +=  int_num[1]
        floated = float(average / devi)
    return floated
