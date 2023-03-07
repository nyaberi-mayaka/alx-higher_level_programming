#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < j:
            print("{:d}{:d}".format(i % 10, j % 10), end="")
            if i == 8 and j == 9:
                print()
                break
            print(", ", end="")
