#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except:
            result = b + a
            continue
    return (result)

from dis import dis
dis(magic_calculation)
