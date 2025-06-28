#!/usr/bin/python3
"""
12-pascal_triangle.py

This module contains a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        # Start each new row with 1
        current_row = [1]
        # Get the previous row to calculate current row elements
        prev_row = triangle[i - 1]

        # Calculate the middle elements of the current row
        # Each element is the sum of the two elements directly above it
        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j + 1])

        # End each new row with 1
        current_row.append(1)
        # Add the completed row to the triangle
        triangle.append(current_row)

    return triangle
