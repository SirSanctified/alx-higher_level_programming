#!/usr/bin/python3
def weight_average(my_list=[]):
    sm = 0
    fs = 0
    avg = 0
    for i in my_list:
        sm += (i[0] * i[1])
        fs += i[1]
    avg = sm / fs
    return avg
