#!/usr/bin/python3
""" Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code"""

from urllib.request import urlopen, Request
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
