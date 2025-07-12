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
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}
    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
