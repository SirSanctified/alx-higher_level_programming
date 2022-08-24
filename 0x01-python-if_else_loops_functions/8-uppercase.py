#!/usr/bin/python3
def uppercase(str):
    result = ''.join([chr(ord(char) - 32) for char in str if ord(char) >= 65])
    print('{}'.format(result))
