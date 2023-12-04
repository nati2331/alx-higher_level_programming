#!/usr/bin/python3
""" 
    This module yeilds true or false
"""


def is_same_class(obj, a_class):
    """
        Function tests if an object is exactly 
        an instance of a specific class.

    Args:
        obj: any object
        a_class: class to test 

    Returns:
        True if obj is an instance of a_class, False if not.

    """
    return (type(obj) == a_class)
