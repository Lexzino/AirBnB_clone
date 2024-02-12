#!/usr/bin/python3
<<<<<<< HEAD
"""Module for FileStorage class."""

import datetime
import json
import os


class FileStorage:

    """Class for storing and retrieving data"""
=======
"""
    Module of file_storage class
"""


import json


class FileStorage():
    """
        Define FileStorage class to serialize and deserialize instances to
        a JSON file and from a JSON file.
    """
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
=======
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
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
<<<<<<< HEAD

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
=======
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as File:
                file_dict = json.load(File)
                cls = '__class__'
                for key, value in file_dict.items():
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
