#!/usr/bin/python3
"""Start by creating a class square """

class Square:
    """A class called square has been created"""

    def __init__(self, size=0):
        """Assigning instance variables
        Args:
            size :size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size is negative
        """

        if not isinstance(size, int):
            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):

        return (self.__size ** 2)
