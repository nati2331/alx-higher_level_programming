#!/usr/bin/python3
""" 
    This modlue creats class with and inherits
    property from (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Inherits from (9-rectangle.py)

        Args:
            size (int): length and width of square

        Attributes:
            __size (int): length of side of square

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
            Computes area of square as size * size.

            Attributes:
                __size (int): length of side of square

            Returns:
                __size ** 2

        """
        return self.__size ** 2
