#!/usr/bin/python3
"""Object oriented program"""


class Square():
    """creating square class"""
    def __init__(self, size=0):
        """the class square has been created
        Args:
           size (int): size of square class
           TypeError: when size is not int
           ValueError: when size is negative
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
