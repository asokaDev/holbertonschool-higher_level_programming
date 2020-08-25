#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as req:
    page = req.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode('utf-8')))
