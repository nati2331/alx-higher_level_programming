#!/usr/bin/python3
"""
    Ceating class base
"""

import json
import os
import csv
import turtle


class Base:
    def __init__(self, id=None):
        """intialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        
        file_name = cls.__name__ + ".json"
        list_ = []
        with open(file_name, "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for i in list_objs:
                    list_.append(i.to_dictionary())
                f.write(Base.to_json_string(list_))

    def from_json_string(json_string):
        
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        
        instance_dict = {}
        for key, val in dictionary.items():
            instance_dict[key] = val
        instance = cls(**instance_dict)
        instance.update(**instance_dict)
        return instance

    @classmethod
    def load_from_file(cls):
        
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        instances_list = []
        with open(file_name, "r", encoding="UTF-8") as f:
            data = f.read()
            dictionary = Base.from_json_string(data)
            for i in dictionary:
                instance = cls.create(**i)
                instances_list.append(instance)
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = cls.__name__ + ".csv"
        with open(file_name, mode="w", newline="") as f:
            write = csv.writer(f)
            if file_name == "Rectangle.csv":
                write.writerow(["id", "width", "height", "x", "y"])
                for obj in list_objs:
                    write.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif file_name == "Square.csv":
                write.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    write.writerow(
                        [obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + ".csv"
        instances = []
        with open(file_name, mode="r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dict = {
                        "id": int(row[0]),
                        "width": int(row[1]),
                        "height": int(row[2]),
                        "x": int(row[3]),
                        "y": int(row[4]),
                    }
                    instances.append(cls.create(**dict))
                elif cls.__name__ == "Square":
                    dict = {
                        "id": int(row[0]),
                        "size": int(row[1]),
                        "x": int(row[2]),
                        "y": int(row[3]),
                    }
                    instances.append(cls.create(**dict))
        return instances

    @staticmethod

    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        for rectangle in list_rectangles:
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
        for square in list_squares:
            for i in range(4):
                t.forward(square.size)
                t.left(90)
        turtle.done()
