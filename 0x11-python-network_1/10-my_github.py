#!/usr/bin/python3
"""Script that takes your Github credentials (username and password) and uses
the Github API to display your id"""
from sys import argv
from requests import get, auth

if __name__ == "__main__":
    req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(req.json().get('id'))
