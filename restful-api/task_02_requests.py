#!/usr/bin/envi python3
"""
this is module
"""


import json
import requests
import csv
"""
this is for using requests
"""


api_url = "https://jsonplaceholder.typicode.com/"


def fetch_and_print_posts():
    """
    this is function
    """
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            posts = response.json()
            for i, post in posts:
                print(f"post title: {post[title]}")
        else:
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"fault: {e}")
    except json.JSONDecodeError:
        print("fail")


def fetch_and_save_posts():
    """
    this is function
    """
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            posts = response.json
            csv_file_name = "posts.csv"
            fieldnames = ['id', 'title', 'body', 'userId']
            with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = posts[0].keys() if posts else []
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for post in posts:
                    writer.writerow(post)
            print(f"{csv_file_name}")
        else:
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"{e}")
    except IOError as e:
        print(f"{e}")
    except json.JSONDecodeError:
        print("error")
