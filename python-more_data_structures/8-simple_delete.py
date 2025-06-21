#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.items():
        del a_dictionary[key]
    else:
        print(a_dictionary)
    return a_dictionary
