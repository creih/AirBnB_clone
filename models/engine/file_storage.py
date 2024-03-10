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
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_value = value.to_dict()  # Convert object to dictionary
            for attr, val in serialized_value.items():
                if isinstance(val, datetime):
                    # Convert datetime to string
                    serialized_value[attr] = val.isoformat()
            serialized_objects[key] = serialized_value

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    for attr, val in value.items():
                        if attr.endswith('_at'):
                            # Convert string to datetime
                            value[attr] = datetime.fromisoformat(val)
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass