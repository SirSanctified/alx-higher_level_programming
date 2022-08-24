def uppercase(str):
    return ''.join([chr(ord(char) - 32) for char in str if ord(char) >= 65])
