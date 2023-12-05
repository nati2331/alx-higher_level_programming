#!/usr/bin/python3
"""
    This is module for task 10.
"""
class Student:
    """
        class form retrieving dictonary.
    """

    def __init__(self, first_name, last_name, age):
        """Initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves dictionary representation
        """

        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value
        return dic
