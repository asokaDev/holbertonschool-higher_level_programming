#!/usr/bin/python3
"""Takes in a letter and sends a POST request with the letter as a
parameter."""
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        d = {'q': argv[1]}
    else:
        d = {'q': ""}
    r = requests.post("http://0.0.0.0:5000/search_user", d)
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
