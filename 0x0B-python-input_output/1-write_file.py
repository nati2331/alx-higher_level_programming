#!/usr/bin/python3
"""
    This module writes string to text file.
"""

def write_file(filename="", text=""):
    """
        Gives no.of lines in a text file.

        Args:
            filename (str): str to be copied
            text: chars to write

    """
with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
