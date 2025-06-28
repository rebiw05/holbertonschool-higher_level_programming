#!/usr/bin/python3
"""
5-save_to_json_file.py

This module contains a function that writes an object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    The file will be created if it doesn't exist.
    Its content will be overwritten if it already exists.

    Args:
        my_obj (object): The object to be serialized to JSON and written.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
