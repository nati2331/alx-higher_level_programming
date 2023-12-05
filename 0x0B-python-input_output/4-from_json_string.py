#!/usr/bin/python3
"""
    function that returns an object
"""
import json

def from_json_string(my_str):
    """
        Returns object from JSON string.

        Args:
            my_obj: The object to be serialized

    """

    return json.loads(my_str)
