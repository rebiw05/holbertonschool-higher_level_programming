#!/usr/bin/python3
"""
this is module
"""


import sys
import urllib.request
import urllib.parse
import urllib.error
"""
this is for using url
"""

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
