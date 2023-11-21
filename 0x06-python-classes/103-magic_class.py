#!/usr/bin/python3
"""docstring"""
import math


class MagicClass:
    """magic good to go"""

    def __init__(self, radius=0):
        """ second docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Third docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Last docstring"""
        return 2 * math.pi * self.__radius
