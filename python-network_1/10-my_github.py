#!/usr/bin/python3
"""Uses GitHub API to display the authenticated user's ID using Basic Auth"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"  # ✅ correct endpoint

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print("None")
