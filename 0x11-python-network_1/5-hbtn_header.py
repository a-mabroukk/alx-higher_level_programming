#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header"""

import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get(argv[1])
    request_id = r.headers.get("X-Request-Id")
    print(request_id)
