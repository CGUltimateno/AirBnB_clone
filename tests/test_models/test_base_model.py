#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import time
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime
from os.path import isfile


class BaseModelTest(TestCase):
    """
    Test cases for BaseModel class
    """

    def test_save(self):
        """
        Testing for save method
        """
        model = BaseModel()
        first = model.updated_at  # Store the initial updated_at datetime

        # Sleep for a short time to ensure a time difference
        time.sleep(1)

        model.save()  # Call save to update the updated_at attribute
        second = model.updated_at  # Get the updated updated_at datetime

        # Compare the dates of the two updated_at attributes
        self.assertNotEqual(first.date(), second.date())
        self.assertTrue(isfile("file.json"))
        self.assertLess(first, second, "Error: save() did not update time")

    def test_to_dict(self):
        """
        Testing for to_dict method
        """
        exp = ("id", "created_at", "updated_at", "__class__")
        model = BaseModel()
        dict = model.to_dict()
        self.assertEqual(sorted(tuple(dict.keys())), sorted(exp))
