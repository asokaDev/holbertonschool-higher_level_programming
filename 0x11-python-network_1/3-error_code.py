#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response """
from sys import argv
from urllib import error, request

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as req:
            print(req.read().decode('utf-8'))
    except error.HTTPError as e:
        err = str(e).split(' ')[2][:-1]
        print("Error code: " + str(err))
