from models.base import Base
from models.square import Square
import unittest

class TestSquare(unittest.TestCase):
    def test_attributes(self):
        obj = Square(1)
        self.assertEqual(obj.size, 1)
        obj = Square(1, 2)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        obj = Square(1, 2, 3)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.id, 4)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_attributes_validation(self):
        with self.assertRaises(TypeError) as traceback:
            Square("a")
        self.assertEqual(str(traceback.exception), "width must be an integer")
        with self.assertRaises(ValueError) as traceback:
            Square(-1)
        self.assertEqual(str(traceback.exception), "width must be > 0")
        with self.assertRaises(TypeError) as traceback:
            Square(1, "a")
        self.assertEqual(str(traceback.exception), "x must be an integer")
        with self.assertRaises(ValueError) as traceback:
            Square(1, -1)
        self.assertEqual(str(traceback.exception), "x must be >= 0")
        with self.assertRaises(TypeError) as traceback:
            Square(1, 2, "a")
        self.assertEqual(str(traceback.exception), "y must be an integer")
        with self.assertRaises(ValueError) as traceback:
            Square(1, 2, -1)
        self.assertEqual(str(traceback.exception), "y must be >= 0")

    def test___str__(self):
        obj = Square(4, 6, 1, 12)
        self.assertEqual(obj.__str__(), "[Square] (12) 6/1 - 4")
        obj_2 = Square(5, 5, 1)
        self.assertEqual(obj_2.__str__(), "[Square] (9) 5/1 - 5")

    def test_update_with_args(self):
        obj = Square(3, 10, 10, 10)
        obj.update(13, 7, 9, 12)
        self.assertEqual(obj.id, 13)
        self.assertEqual(obj.size, 7)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
        obj.update(6, 5)
        self.assertEqual(obj.id, 6)
        self.assertEqual(obj.size, 5)

    def test_update_with_kwargs(self):
        obj = Square(3, 10, 10, 10)
        obj.update(id=11, size=5, x=9, y=12)
        self.assertEqual(obj.id, 11)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 9)
        self.assertEqual(obj.y, 12)
        obj.update(size=30, x=10, y=2)
        self.assertEqual(obj.id, 11)
        self.assertEqual(obj.size, 30)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, 2)

    def test_update_with_dictionnary(self):
        obj = Square(3, 10, 10, 10)
        obj.update(**{'id': 89})
        self.assertEqual(obj.id, 89)
        obj.update(**{'id': 89, 'size': 1})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 1)
        obj.update(**{'id': 89, 'size': 2})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 2)
        obj.update(**{'id': 89, 'size': 2, 'x': 3})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        obj.update(**{'id': 89, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_to_dictionary(self):
        obj = Square(10, 2, 1, 9)
        self.assertIsInstance(obj.to_dictionary(), dict)

