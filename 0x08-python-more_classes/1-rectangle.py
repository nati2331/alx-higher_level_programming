#!/usr/bin/python3

class Rectangle:
    """A rectangle class is created."""

    def __init__(self, width=0, height=0):
        """
            Objects Intialization
            Args:
                width (int): Width of rectangle.
                height (int): Height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Gets instance from class"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
