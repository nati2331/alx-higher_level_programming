#!/usr/bin/python3
"""creating a class called square"""


class Square():
    """square class has been created"""

    def __init__(self, size=0):
        self.__size = size
    @property
    def size(self):
        """Find the value of size
        Args:
            size: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
    
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """To find area of square
        Returnss: are of square
        """
        return self.__size ** 2
