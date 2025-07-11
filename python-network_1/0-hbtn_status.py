#!/usr/bin/python3
"""
this is module
"""


import urllib.request
"""
this is for using url
"""

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {
        'cfclearance': 'true'
    }
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
