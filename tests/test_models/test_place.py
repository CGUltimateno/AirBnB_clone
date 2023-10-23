#!/usr/bin/python3
"""
Unittest for Place class
"""
from unittest import TestCase
from models.place import Place
from datetime import datetime

class PlaceTest(TestCase):
    """
    Test cases for Place class
    """
    def test_new_instance(self):
        """
        Testing for new instance
        """
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])