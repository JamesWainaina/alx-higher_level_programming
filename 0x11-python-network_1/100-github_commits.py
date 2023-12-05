#!/usr/bin/python3
"""The Holberton School staff evaluates candidates
applying for a back-end position with multiple
technical challenges, like this one:
Write a Python script that takes 2 arguments in order
to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys"""

from sys import argv
import requests

if __name__ == "__main__":
    usr = argv[2]
    rep = argv[1]
    url = "https://api.github.com/repos/" + usr + "/" + rep + "/commits"
    r = requests.get(url)
    result = r.json()

    for i  in range(10):
        sh = result[i].get("sh")
        author_name = result[i].get("commit").get("author").get("name")
        print("{}: {}".format(sh,author_name))
