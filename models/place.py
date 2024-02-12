#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a Place class"""

=======
"""Place module
"""
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """Class for managing place objects"""

=======
    """Define place class
    """
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
