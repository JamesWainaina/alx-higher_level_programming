#!/usr/bin/python3

""" Write a Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        de_html = html.decode()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\
\t- utf8 content: {}".format(type(html), html, de_html))
