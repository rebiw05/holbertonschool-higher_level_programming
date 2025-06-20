#!/usr/bin/python3
def number_keys(a_dictionary):
    key_numbers = []
    for key, value in a_dictionary.items():
        key_numbers.append(key)
    return len(key_numbers)
