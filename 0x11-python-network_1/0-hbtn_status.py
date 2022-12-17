#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status using urllib package
"""


import urllib.request


if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        data = res.read()
        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {data.decode()}')
