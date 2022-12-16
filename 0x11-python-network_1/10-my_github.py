#!/usr/bin/python3
""" This module contains a script to check github credentials """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=HTTPBasicAuth(username, password))
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print('None')
