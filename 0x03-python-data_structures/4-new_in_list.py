#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx in range(0, len(my_list)):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    return my_list
