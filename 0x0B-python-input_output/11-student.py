#!/usr/bin/python3
"""Module for question 11"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
            Initialization.

            Args:
                first_name (str): The first name.
                last_name (str): The last name.
                age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Get a dictionary representation of the Student.

            If attrs is a list of strings, represents only those attributes
            included in the list.

            Args:
                attributes: attributes to represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
            Replace all attributes of the Student.

            Args:
                json (dict): value to replace attribute.
        """
        for k, v in json.items():
            setattr(self, k, v)
