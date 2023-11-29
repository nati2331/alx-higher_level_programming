#!/usr/bin/python3

""" Answer for question 6 """


class Rectangle:

    """
    initialize Obects
    width (int): width of rectangle
    height (int): height of rectangle
    """

    number_of_instances = 0
    "track number rectangle"

    def __init__(self, width=0, height=0):
        """ Initialize instance """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Gets the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @property
    def height(self):
        """ get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    def area(self):
        """ compute rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ compute perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((2 * self.__height)+(2 * self.__width))

    def __str__(self):
        """ returns string repsentation """
        if self.__height == 0 or self.__width == 0:
            return ""

        print_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                print_str += "#"
            if i != self.__height - 1:
                print_str += "\n"
        return print_str

    def __repr__(self):
        """ return a string representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ when object is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
