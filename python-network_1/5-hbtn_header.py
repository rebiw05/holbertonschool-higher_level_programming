#!/usr/bin/python3
"""
this is module
"""


import sys
import requests
"""
this is for using url
"""


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {"cfclearance": "true"}
    response = requests.get(url, headers=headers)
    print(response.headers.get("X-Request-Id"))
