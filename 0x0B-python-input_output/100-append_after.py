#!/usr/bin/python3
"""
    function inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
        inserts text after a line

        Args:
            filename (str):name of the file.
            search_string (str): The string to search.
            new_string (str): new string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
