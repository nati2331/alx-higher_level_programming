#!/usr/bin/python3

"""
    This module checks if an object is an
    instance of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
        Test if Object is an instance of class
        or inherited class.

        Args:
            obj (any): the object to check
            a_class (Class): class to check against
        Returns:
            True: if isinstance othewise false
    """

    return True if isinstance(obj, a_class) else False
