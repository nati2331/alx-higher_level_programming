#!/usr/bin/python3
"""
    Answer to question 7
"""


class Rectangle:
    """
        Creates Rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        """
            Initializion of Objects 
            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
        """
            returns string representation 
        """
        if self.__width == 0 or self.__height == 0:
            return ''

        length = list()
        for i in range(self.__height):
            for j in range(self.__width):
                length.append(str(self.print_symbol))
            if i + 1 != self.__height:
                length.append('\n')
        return ''.join(length)

    def __repr__(self) -> str:
        """
            returns string representation 
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
            used when instance is getting deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
            Gets the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
            Gets the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """
            calculate the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            calculate the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
