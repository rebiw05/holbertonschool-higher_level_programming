#!/usr/bin/python3
"""
this serialize and deserilize the file.

Attributes:
    with open: for opening file
    .dump and .load: serilizing and deserializing the file
"""
import json
"""
this import json attributes
"""


def serialize_and_save_to_file(data, filename):
    """
    this is function
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    this is functoin
    """
    with open(filename, "r") as f:
        return json.load(f)
