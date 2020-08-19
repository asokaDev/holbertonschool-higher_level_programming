#!/bin/bash
# Get the methods that the server permits

curl --silent --head "$1" | grep Allow | cut --delimiter ' ' -f 2-
