#!/usr/bin/python3
"""
Unittest for Amenity class
"""
from unittest import TestCase
from models.amenity import Amenity
from datetime import datetime


class UserTest(TestCase):
    """
    Test cases for Amenity class
    """

    def test_new_instance(self):
        """
        Testing for new instance
        """
        self.assertEqual(Amenity.name, "")
