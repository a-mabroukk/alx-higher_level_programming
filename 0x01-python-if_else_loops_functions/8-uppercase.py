#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(c) >= 65 and ord(c) <= 90:
            print("{}".format(c), end="")
        print()
