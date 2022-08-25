#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    names = []
    for i in dir(hidden_4):
        if not i.startswith('__'):
            names.append(i)
    names.sort()
    for i in names:
        print(i)
