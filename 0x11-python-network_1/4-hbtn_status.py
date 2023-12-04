#!/usr/bin/python3
"""Write a Python script that fetches
https://alx-intranet.hbtn.io/status
You must use the package requests """

import requests

if __name__ == "__main__":

    req = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:\n\t- type: {}\n\t- \
content: {}".format(type(req.text), req.text))
