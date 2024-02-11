#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.base_model import BaseModel
from models.user import User


class Testuser(unittest.TestCase):

    def test_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
