#!/usr/bin/python3
"""
module to serialize instances to JSON file and deserialization JSON
file to instances
"""
import json


Class FileStorage:
    """ class to serialize the other class' s instances to/from file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method to return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets __objects obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialises __objects to Json file."""
        with open(self.__file_path, 'w') as fil:
            json.dumps(self.__objects, fil)

    def reload(self):
        """deserialises Json file to __objects."""
        try:
            with open(self.__file_path, 'r') as fil:
                self.__objects = json.load(fil)
        except FileNotFoundError:
            pass
