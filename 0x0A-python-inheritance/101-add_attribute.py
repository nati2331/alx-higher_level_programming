#!/usr/bin/python3
""" 
    Module for task 13 
"""


def add_attribute(obj, attribute, value):
    """
        replaces `attribute` with `value`.

        Args:
            obj : object to have attribute set
            attribute: name of new attribute
            value: value to set attribute

        Raises:
            TypeError: If adding attribute not possible.

    """
    if hasattr(obj, "__dict__"):
        # if __dict__ is present, attributes can be dynamically added
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        # even if no __dict__, existing attributes in __slots__ can be updated
        setattr(obj, attribute, value)
    else:
        # out of options, can't add
        raise TypeError("can't add new attribute")
