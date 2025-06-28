#!/usr/bin/python3
"""
this module defines subclass obj
"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
