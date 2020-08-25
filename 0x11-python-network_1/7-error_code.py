#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response."""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
