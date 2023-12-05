#!/usr/bin/python3
"""Write a Python script that takes in a
letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:

    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        data = {"q": ""}
    elif not isinstance(argv[1], str):
        print("No result")
    else:
        data = {"q": argv[1]}

    req = requests.post('http://0.0.0.0:5000/search_user', data = data)
    try:
        result = req.json()
        r_id = result.get('id')
        name = result.get('name')
        if len(result) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r_id, name))
    except ValueError:
        print("Not a valid JSON")