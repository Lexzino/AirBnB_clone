#!/usr/bin/python3
"""
Test State
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Teststate(unittest.TestCase):
    def test_pep8_conformance_state(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_class(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        my_state.name = "Antioquia"
        self.assertEqual(my_state.name, 'Antioquia')
