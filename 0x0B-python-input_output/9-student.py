#!/usr/bin/python3
"""
     class Student that defines a student by name and age
"""
class Student:
    """
        class student is created.
    """
    def __init__(self, first_name, last_name, age):
        """
            initialize ojects
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            function retrieves dictonary rep of students
        """
        return self.__dict__
