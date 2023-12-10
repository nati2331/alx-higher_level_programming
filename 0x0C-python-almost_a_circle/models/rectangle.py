#!/usr/bin/python3
"""
0x0C. Python - Almost a circle
"""

from models.base import Base


class Rectangle(Base):
    """
        Task 2 to 13 are solved by inheritance
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """creates new instance of rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)   

    @property
    def width(self):
        """allows to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """allows to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """allows to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets heights incase of change"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retireves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y retriever"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ computes area"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle with # char"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for o in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        
        attribute_names = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(min(len(attribute_names), len(args))):
                setattr(self, attribute_names[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in attribute_names:
                    setattr(self, key, val)

    def to_dictionary(self):
        
        dict = {'id': self.id,
                       'width': self.width,
                       'height': self.height,
                       'x': self.x,
                       'y': self.y}
        return (dict)
