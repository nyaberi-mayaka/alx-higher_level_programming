#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    elif idx > len(my_list) - 1:
        return (my_list)

    else:
        new_list = my_list.copy()
        new_list[idx] = element
        # could also use new_list = list(my_list)
        return (new_list)
