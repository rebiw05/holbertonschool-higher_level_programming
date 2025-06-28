#!/usr/bin/python3
"""
8-class_to_json.py

This module contains a function that returns the dictionary
description with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary containing serializable attributes of the object.
    """
    return obj.__dict__
