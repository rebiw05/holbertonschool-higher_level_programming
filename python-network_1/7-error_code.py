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
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", response.status_code)
