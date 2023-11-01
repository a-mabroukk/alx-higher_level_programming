#!/usr/bin/python3
for n in range(0, 10, 1):
    for n2 in range(1, 10, 1):
        if n2 > n and n != 8:
            print("{}{}".format(n, n2), end=", ")
        elif n == 8 and n2 == 9:
            print("{}{}".format(n, n2))
        break
