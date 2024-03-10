#!/usr/bin/python3
"""
this file ni iyo kubika objects 
"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this all method niya displaying objects zose."""
        return self.__objects

    def new(self, obj):
        """this new method niya creating new objects."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """this save method niya keeping objects."""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """this reload method niya rerunning objects nanone."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
