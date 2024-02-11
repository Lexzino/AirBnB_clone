#!/usr/bin/python3
"""
    This is the module of the BaseModel class.
    Which will be used as a Base-class for AirBnb
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """
        Define BaseModel class.
    """
    def __init__(self, *args, **kwargs):
        """
            Initialisation method
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            String representation of class instance method
        """
        name = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(name, self.id, self.__dict__)

    def save(self):
        """
            Method to update date.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Method to return dictionary.
        """
        name = self.__class__.__name__
        New_dict = self.__dict__.copy()
        New_dict.update(__class__=name, created_at=self.created_at.isoformat())
        New_dict.update(updated_at=self.updated_at.isoformat())

        return New_dict
