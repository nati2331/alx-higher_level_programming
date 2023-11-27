#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """ 
    Function prints My name is <first name> <last name>

    Args:
        first_name: First name.
        last_name: Last name.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
