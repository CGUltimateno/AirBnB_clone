#!/usr/bin/python3
"""
Unittest for City class
"""
from unittest import TestCase
from models.city import City
from datetime import datetime


class CityTest(TestCase):
    """
    Test cases for City class
    """

    def test_new_instance(self):
        """
        Testing for new instance
        """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
