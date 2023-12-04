#!/usr/bin/python3
"""
    Module has class Rectangle and inherits
    from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Inherits tests from BaseGeometry
    """

    def __init__(self, width, height):
        """
            Initialize the class
            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
