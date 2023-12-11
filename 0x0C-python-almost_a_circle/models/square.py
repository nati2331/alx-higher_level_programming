#!/usr/bin/python3

"""
    creating class square
"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Initialization

        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int): x.
            y (int): y.
            id (int): id of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
    """        
        Initalization

        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int): x.
            y (int): y.
            id (int): id of square.
    """
       
       attribute_names = ["id", "size", "x", "y"]
        for i in range(min(len(attribute_names), len(args))):
            setattr(self, attribute_names[i], args[i])

        for key, value in kwargs.items():
            if key in attribute_names:
                setattr(self, key, value)

    def __str__(self):
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """
            Sets size in case of change.
            Raises:
                TypeError: if width is not an integer.
                ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        
        if args:
            for i in range(min(len(attribute_names), len(args))):
                setattr(self, attribute_names[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in attribute_names:
                    setattr(self, key, val)
    def to_dictionary(self):
        
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
