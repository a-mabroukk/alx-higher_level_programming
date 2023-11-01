#!/usr/bin/python3
for n in range(0, 10, 1):
    for n2 in range(1, 10, 1):
        if n >= n2:
            continue
        elif n == 8 and n2 == 9:
            print("{}{}".format(n, n2))
        else:
            print("{}{}".format(n, n2), end=", ")
