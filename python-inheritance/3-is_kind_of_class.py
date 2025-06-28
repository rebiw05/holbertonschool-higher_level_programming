#!/usr/bin/python3
"""
This module ilustrates obj that exist
in specifc class and its subs
"""


def is_kind_of_class(obj, a_class):
    """
    is kin of class function
    """
    if not isinstance(obj, a_class):
        return False
    return True
