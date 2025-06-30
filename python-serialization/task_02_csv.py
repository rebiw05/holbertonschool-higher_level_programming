#!/usr/bin/python3
"""
this is module
"""


import csv
"""
this helps to use csv files
"""


import json
"""
this helps to serialize json files
"""


def convert_csv_to_json(csv_filename):
    """
    this is function
    """
    try:
        with open(data.csv, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        with open(data.json, mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception as e:
        print(f"file not found{e}")
        return False
