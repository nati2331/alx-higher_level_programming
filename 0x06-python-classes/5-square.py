#!/usr/bin/python3
class Square:
    """Class called square is created"""
    def __init__(self, size=0):
        """Assign instace variables
        Args:
            size: size of square
            Raise:
                ValueError: if size is negative
                TypeError: if size is non integer
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)

