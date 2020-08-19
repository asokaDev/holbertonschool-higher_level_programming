#!/bin/bash
# Using POST send a json to validate

curl --silent --header "Content-Type: application/json" --request POST --data @"$2" "$1"
