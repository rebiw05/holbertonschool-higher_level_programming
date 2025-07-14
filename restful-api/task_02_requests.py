#!/usr/bin/envi python3
"""
this is module
"""


import requests
import csv
"""
this is for using requests
"""


api_url = "https://jsonplaceholder.typicode.com/"
response = requests.get(api_url)


def fetch_and_print_posts():
    """
    this is function
    """
    if response.status_code == 200:
        posts = response.json()
        for i, post in posts:
            print(f"post title: {post[title]}")
    else:
        print(response.status_code)


def fetch_and_save_posts():
    """
    this is function
    """
    if response.status_code == 200:
        csv_file_name = "posts_data.csv"
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
            fieldnames = posts[0].keys() if posts else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow(post)
        print(f"{csv_file_name}")
    else:
        print(response.status_code)
