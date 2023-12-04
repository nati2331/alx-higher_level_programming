#!/usr/bin/python3
"""
    Module inherits for task 12
"""


class MyInt(int):
    """
        Inherits from int
    """

    def __init__(self, num):
        """
            Initializing MyInt
            Args:
                num: Given int
        """

        self.num = num

    def __eq__(self, value):
        """
            Inverts == to !=
            Returns: Either true or false
        """

        if not isinstance(value, MyInt):
            return False

    def __ne__(self, value):
        """
            Inverts != to ==
            Returns: Either true or false
        """

        if not isinstance(value, MyInt):
            return True
