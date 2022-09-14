#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in my_list:
        try:
            if n == x:
                print()
                break
            print("{:d}".format(i), end="")
            n += 1
        except ValueError as er:
            pass
