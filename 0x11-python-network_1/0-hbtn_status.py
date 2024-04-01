#!/usr/bin/python3
"""importing urllib package to fetch URL"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    as response:
        respon = response.read()

        print("- type: ", type(respon))
        print("- content: ", respon)
        print("- utf8 content: ", respon.decode())
