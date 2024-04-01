#!/usr/bin/python3
"""importing modules to take in a URL, sends a request to the URL and
displays the value of variable found in the header of the response"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers
    request_id = headers['X-Request-Id']
    print(f"{request_id}")
