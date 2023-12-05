#!/usr/bin/python3
"""
    Outputs string from JSON string
"""
import json

def load_from_json_string(filename):
    """
        Outputs an object represented by a JSON str.

    """
    with open(filename) as f:
        return json.loads(f)
