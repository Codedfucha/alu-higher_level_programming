#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of a 200 status code response
curl -sL -X GET "$1"
