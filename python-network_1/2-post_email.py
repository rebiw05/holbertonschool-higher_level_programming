#!/usr/bin/python3
"""Sends a POST request with email and displays the response body (utf-8 decoded)."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode POST data
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    # Create and send the POST request
    req = urllib.request.Request(url, data)

    # Send the request using with statement
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
