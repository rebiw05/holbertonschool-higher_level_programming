#!/usr/bin/python3
"""
this is module
"""


import requests
"""
this is for fetching
"""


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {"cfclearance": "true"}
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type:".format(type(content)))
    print("\t- content:".format(content))
