#!/usr/bin/python3
""" 
    This module checks if an object is an
    instance of class inhertied.
"""


def inherits_from(obj, a_class):
    """
        Returns True if the object is an instance 
        of a class that inherited (directly or indirectly) 
        from the specified class, otherwise False.

    Args:
        obj : object of any type
        a_class (class): class to test against

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise.

    """
    if type(obj) == a_class:
        return (False)
    return (issubclass(type(obj), a_class))
