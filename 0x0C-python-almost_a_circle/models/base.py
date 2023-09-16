#!/usr/bin/python3
import json
import csv
import os.path

class Base:
    """base class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """initializing instances"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ adding the static method that returns the JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """save json in a file"""
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                lst = [a.to_dictionary() for a in list_objs]
                jfile.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ JSON to dictionary """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            x = cls(5, 5)
        else:
            x = cls(5)
        x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        name = str(cls.__name__) + ".json"
        try:
            with open(name, "r") as jsonfile:
                list = Base.from_json_string(jsonfile.read())
                return [cls.create(**a) for a in list]
        except IOError:
            return []
