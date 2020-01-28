#!/usr/bin/python3
"""This module define the Base class"""
import os
import json


class Base:
    """Define the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        lista = []
        if list_objs is not None:
            for i in list_objs:
                lista.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 8)
        if cls.__name__ == "Square":
            dummy = cls(9)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        fname = cls.__name__ + ".json"
        lista = []
        if os.path.isfile(fname):
            with open(fname, 'r') as file:
                cont = cls.from_json_string(file.read())
                for elem in cont:
                    lista.append(cls.create(**elem))
                return lista
        else:
            return []
