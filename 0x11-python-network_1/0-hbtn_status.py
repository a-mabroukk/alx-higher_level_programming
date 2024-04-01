#!/usr/bin/python3
"""importing urllib package to fetch URL"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    respon = response.read()

    print("Body response:")
    print("\t- type: ", type(respon))
    print("\t- content: ", respon)
    print("\t- utf8 content: ", respon.decode('utf-8'))
