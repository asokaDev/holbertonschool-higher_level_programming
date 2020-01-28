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
