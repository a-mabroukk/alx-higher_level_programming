#!/bin/bash
#script that takes in a URL and displays the body of the response
curl -s -w "%{http_code}" -L "$1"