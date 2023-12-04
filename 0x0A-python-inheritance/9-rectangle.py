#!/usr/bin/python3
"""
    This module inherits property from both task 7 and 8
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Inherits from BaseGeometry to construct rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Attributes:
            __width (int): width of rectangle
            __height (int): height of rectangle

    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            Computes area of rectangle.

        Attributes:
            __width (int): width of rectangle
            __height (int): height of rectangle

        Returns:
            __width * __height

        """
        return self.__width * self.__height

    def __str__(self):
        """ 
            Gives the area of the rectangle.

        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
