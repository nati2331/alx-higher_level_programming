#!/usr/bin/python3
""" 
    This module validate value and raises errors.
"""


class BaseGeometry:
    """
        Left empty area() method.

    """
    def area(self):
        """
            Raises exception for user.

        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            validates the value

        Args:
            name : name of object
            value : value of object, cant't be int

        Exceptions:
            TypeError: if value is not an integer
            ValueError: if value is <= 0

        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
