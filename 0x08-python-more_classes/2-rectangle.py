#!/usr/bin/python3

""" Rectangel Class is created. """


class Rectangle:

    """
    Object intinalization
    width (int):
    height (int)
    """
    def __init__(self, width=0, height=0):
        """ Instance data """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width to a new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        """ gets height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ set heightto a new """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    def area(self):
        """ Compute rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ Compute perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((2 * self.__height)+(2 * self.__width))
