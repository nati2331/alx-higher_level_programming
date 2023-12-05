#!/usr/bin/python3
"""
    Function appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
        function appends a string
        and returns the number of characters added
    """
    with open(filename, "a", encoding='UTF-8') as myfile:
        fc = myfile.write(text)
        return fc
