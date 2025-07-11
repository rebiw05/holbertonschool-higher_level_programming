#!/usr/bin/python3
"""
this displays the x id value
"""


import sys
import urllib.request
"""
this is for using url and terminal coding
"""


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
