#!/usr/bin/python3
""" This module returns a list of
    attributes and methods of an object.
"""


def lookup(obj):
    """
        Function gives the list of available
        attributes and methods of an object
        Args:
            obj(obj) - the object
        Returns:
        list: list of every attributes and method
    """

    return dir(obj)
