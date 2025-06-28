#!/usr/bin/python3
"""
6-load_from_json_file.py

This module contains a function that creates an object
from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
