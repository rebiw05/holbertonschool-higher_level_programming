#!/usr/bin/python3
"""
2-append_write.py

This module contains a function to append a string to a text file.
"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns chars added.

    Creates the file if it doesn't exist.

    Args:
        filename (str): Name of the file.
        text (str): String content to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        num_characters_added = f.write(text)
        return num_characters_added
