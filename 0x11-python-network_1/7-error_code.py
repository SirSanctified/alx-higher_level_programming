#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of
the response.
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""

import sys
import requests

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code < 400:
        print(res.text)
    else:
        print(f'Error code: {res.status_code}')
