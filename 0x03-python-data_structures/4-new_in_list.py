#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    modi_list = my_list.copy()
    if idx < 0:
        return modi_list
    elif idx >= len(my_list):
        return modi_list
    else:
        modi_list[idx] = element
        return modi_list
