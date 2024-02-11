#!/usr/bin/python3
"""
    Module of file_storage class
"""


import json


class FileStorage():
    """
        Define FileStorage class to serialize and deserialize instances to
        a JSON file and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Method to return the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        FileStorage.__objects[obj_name + '.' + obj_id] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as File:
            json.dump(new_dict, File)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as File:
                file_dict = json.load(File)
                cls = '__class__'
                for key, value in file_dict.items():
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
