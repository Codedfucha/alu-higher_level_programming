#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id variable from the response headers. "
This script takes a URL as a command-line argument, sends an HTTP request to the URL,
and displays the value of the 'X-Request-Id' variable found in the header of the response.

Usage:
    ./1-hbtn_header.py <URL>

Arguments:
    <URL> : The URL to which the request is sent. This URL must be accessible and should respond with appropriate headers.

Dependencies:
    - urllib.request : For sending HTTP requests and handling responses.

Example:
    $ ./1-hbtn_header.py https://intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            print(headers.get("X-Request-Id", "Header not found"))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
