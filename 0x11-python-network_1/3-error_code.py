#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
have to manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""

import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode(encoding='utf8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.getcode()}')
