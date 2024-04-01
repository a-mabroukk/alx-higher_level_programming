#!/usr/bin/python3
"""importing urllib package to fetch URL"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    respon = response.read()

    print("Body response:")
    print("- type: ", type(respon))
    print("- content: ", respon)
    print("- utf8 content: ", respon.decode('utf-8'))
