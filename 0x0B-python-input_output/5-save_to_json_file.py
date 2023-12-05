#!/usr/bin/python3
""" brings the Json properties."""
import json


def save_to_json_file(my_obj, filename):
    """
        prints object to a text file 
        using JSON representation.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
