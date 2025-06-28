#!/usr/bin/python3
"""
1-write_file.py

This module contains a function to write a string to a text file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns characters written.

    Creates or overwrites the file.

    Args:
        filename (str): Name of the file.
        text (str): String content to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        num_characters_written = f.write(text)
        return num_characters_written
