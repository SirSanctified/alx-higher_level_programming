#!/usr/bin/python3
""" This module contains a script to fetch a URL """
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    post_add = {"q": q}
    r = requests.post(url, data=post_add)
    try:
        js = r.json()
        if len(js) == 0:
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except Exception:
        print("Not a valid JSON")
