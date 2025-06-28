#!/usr/bin/python3
"""
7-add_item.py

This script adds all command-line arguments to a Python list,
and then saves this list to a file named 'add_item.json' in JSON format.
If 'add_item.json' already exists, it loads the existing items first,
then appends the new arguments before saving.
"""
import sys
import os.path

# Import the necessary functions from previous modules.
# Assuming '5-save_to_json_file.py' and '6-load_from_json_file.py'
# are in the same directory or accessible via Python path.
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename for storing the JSON list.
filename = "add_item.json"

# Initialize an empty list to hold the items.
# This list will be populated from the file if it exists,
# or remain empty if the file doesn't exist or is invalid.
items = []

# Check if the file exists and has valid JSON content.
if os.path.exists(filename):
    try:
        # Attempt to load existing items from the JSON file.
        items = load_from_json_file(filename)
    except ValueError:
        items = []

for arg in sys.argv[1:]:
    items.append(arg)

# Save the updated list back to the JSON file.
save_to_json_file(items, filename)
