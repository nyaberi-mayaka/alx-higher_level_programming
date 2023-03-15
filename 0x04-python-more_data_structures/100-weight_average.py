#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    total_sum = 0
    weight = 0
    for tuple_a in my_list:
        multiplied = 1
        for i in tuple_a:
            multiplied *= i
        total_sum += multiplied
        weight += tuple_a[1]
    return (total_sum / weight)
