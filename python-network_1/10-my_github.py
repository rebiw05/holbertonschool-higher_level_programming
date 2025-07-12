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
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://github.com/rebiw05"
    response = requests.get(url, auth=(username, token))
    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print("None")
