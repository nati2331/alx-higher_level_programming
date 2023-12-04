#!/usr/bin/python3
"""
    This module tests for exception
"""


class BaseGeometry:
    """
        Left empty area() method.
    """
    def area(self):
        """
            Only raises exception for user.

        """
        raise Exception('area() is not implemented')
