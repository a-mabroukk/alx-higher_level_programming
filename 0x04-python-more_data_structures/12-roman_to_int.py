#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000}

    if type(roman_string) is not str:
        return 0
    int_value = 0
    prev_value = 0
    
    for character in roman_string:
        current_value = roman_num_dic[character]
        if current_value <= prev_value:
            int_value += current_value
        else:
            int_value -= prev_value
            int_value += current_value
        prev_value =  current_value
    return int_value
