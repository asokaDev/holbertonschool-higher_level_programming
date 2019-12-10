#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        if b > a:
            print("{:d}{:d}".format(a, b), end="")
            if a < 8:
                print("", end=", ")
            else:
                print("")
