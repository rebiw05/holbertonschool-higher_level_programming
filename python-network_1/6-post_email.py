#!/usr/bin/python3
"""
this is module
"""


import requests
import sys
"""
this is for using url
"""

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email" : email}
    response = requests.post(url, data)
    print("Your email is: {}".format(response.text))
