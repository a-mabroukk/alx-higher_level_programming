#!/usr/bin/python3
"""importing modules to take in a URL, sends a request to the URL and
displays the value of variable found in the header of the response"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        headers = response.info()
        request_id = headers['X-Request-Id']
        print(request_id)
