#!/usr/bin/python3
def print_square(size):
    # size must be an integer, otherwise raise a TypeError
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    # if size is less than 0, raise a ValueError
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        print('#' * size)
