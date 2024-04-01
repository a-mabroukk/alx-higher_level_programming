#!/usr/bin/python3
"""Fetching url and status code"""

import requests

response = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
