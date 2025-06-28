#!/usr/bin/python3
"""
0-read_file.py

This module contains a function to read a text file and print its content.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout.
    """
    # Open the file in read mode ('r') with UTF-8 encoding.
    # The 'with' statement ensures the file is properly closed after its block,
    # even if errors occur.
    with open(filename, mode='r', encoding='utf-8') as f:
        # Read the entire content of the file.
        file_content = f.read()
        # Print the content to standard output.
        print(file_content, end="")
