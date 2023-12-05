#!/usr/bin/python3
"""
    This function reads files and print them.
"""


def read_file(filename=""):
    """
        Print text to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
