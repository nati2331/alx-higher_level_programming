#!/usr/bin/python3
"""
    Module for task 12
"""


class MyInt(int):
    """
        Inherits 9-rectangle.py and 10-square.py 
        inverting == and !=
    """

    def __init__(self, num):
        """
            Initialize object MyInt
            Args:
                num: int given
        """

        self.num = num

    def __eq__(self, value):
        """
            Inverts == to !=
            Returns: true or false
        """

        if not isinstance(value, MyInt):
            return False

    def __ne__(self, value):
        """
            Inverts != behaviour
        """

        if not isinstance(value, MyInt):
            return True
