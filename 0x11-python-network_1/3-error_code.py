#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
the URL and displays the body of the response"""

import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as reques:
            print(reques.read().decode('utf-8'))
    except urllib.error.HTTPError as errors:
        print(f"Error code: {errors.code}")
