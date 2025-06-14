#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints the last digit of a number and returns its value.

    Args:
        number (int): The integer whose last digit is to be printed and returned.

    Returns:
        int: The value of the last digit of the number.
    """
    absolute_number = abs(number)
    last_digit = absolute_number % 10
    print(last_digit, end="")
    return last_digit
