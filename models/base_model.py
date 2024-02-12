#!/usr/bin/python3
<<<<<<< HEAD
"""The base model" script """

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """ The class inheriter of all other classes"""

    def __init__(self, *args, **kwargs):
        """Initializing instance attributes
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
=======
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
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
<<<<<<< HEAD
        """Returns string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updating the public instance attribute updated_at"""

=======
        """
            String representation of class instance method
        """
        name = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(name, self.id, self.__dict__)

    def save(self):
        """
            Method to update date.
        """
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """returns the dictionary holoding all values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
=======
        """
            Method to return dictionary.
        """
        name = self.__class__.__name__
        New_dict = self.__dict__.copy()
        New_dict.update(__class__=name, created_at=self.created_at.isoformat())
        New_dict.update(updated_at=self.updated_at.isoformat())

        return New_dict
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
