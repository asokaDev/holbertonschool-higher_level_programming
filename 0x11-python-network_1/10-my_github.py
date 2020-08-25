#!/usr/bin/python3
""""""
from sys import argv
from requests import get, auth

if __name__ == "__main__":
    req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
