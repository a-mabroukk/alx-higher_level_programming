#!/bin/bash
# sript that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -w "$1" "%{http_code}" -o /dev/null