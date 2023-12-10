from models.base import Base
from models.rectangle import Rectangle
import unittest

class TestBase(unittest.TestCase):
    def test_id(self):
        obj_base = Base()
        self.assertIsInstance(obj_base, Base)
        obj_base.id = 2
        self.assertEqual(obj_base.id, 2)

    def test_to_json_string(self):
        obj_base = Base()
        json_str = obj_base.to_json_string({'x': 2, 'width': 10, 'id': 1})
        self.assertEqual(json_str, '{"x": 2, "width": 10, "id": 1}')

    def test_from_json_string(self):
        list_input = [{'height': 2, 'width': 1, 'id': 77}]
        json_str = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_output, list_input)

    def test_create(self):
        obj = Rectangle(3, 5, 1)
        obj_dict = obj.to_dictionary()
        obj_creation = Rectangle.create(**obj_dict)
        self.assertEqual(str(obj_creation), "[Rectangle] (1) 1/0 - 3/5")

if __name__ == "__main__":
    unittest.main()
