#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = len(argv)
    if args == 2:
        print('{} argument'.format(args - 1))
    else:
        print('{} arguments'.format(args - 1))
    for i in range(1, args):
        print('{}: {}'.format(i, argv[i]))
