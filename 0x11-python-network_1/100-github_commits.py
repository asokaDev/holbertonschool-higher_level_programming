#!/usr/bin/python3
""" Interview challenge """
from requests import get
from sys import argv


if __name__ == "__main__":
    req = get("https://api.github.com/repos/{}/{}/commits".
               format(argv[2], argv[1])).json()
    num = 0
    for val in req:
        num += 1
        name = val.get("commit").get("author").get("name")
        sha = val.get("sha")
        print("{}: {}".format(sha, name))
        if num == 10:
            break
