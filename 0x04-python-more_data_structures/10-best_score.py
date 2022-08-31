#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bk = -1
    for i in a_dictionary.keys():
        if a_dictionary[i] > bk:;
            bk = a_dictionary[i]
    return bk

