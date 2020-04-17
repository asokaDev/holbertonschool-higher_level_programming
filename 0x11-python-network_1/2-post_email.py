#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8)"""
from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode()
    with request.urlopen(argv[1], data) as req:
        print(req.read().decode('utf-8'))
