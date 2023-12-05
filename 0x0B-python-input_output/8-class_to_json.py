#!/usr/bin/python3
"""
    Function  returns the dictionary description.
"""


def class_to_json(obj):
    """Function returns the dictionary represntation with a simple data structure."""
    return obj.__dict__
