#!/usr/bin/python3
"""importing modules to take in a URL, sends a request to the URL and
displays the value of variable found in the header of the response"""
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        request_id = headers['X-Request-Id']
        print(request_id)
