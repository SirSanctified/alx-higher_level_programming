#!/usr/bin/python3

"""
    Define a function called print_sorted inside MyList class
    which inherits from the built-in list class,
    that prints the elements of MyList
    in sorted ascending order
"""


class MyList(list):
    """
        Inherit the list class and extend its functionality
    """

    def print_sorted(self):
        """
            Print this list in sorted order
        """
        nw = self.copy()
        nw.sort()
        print(nw)
