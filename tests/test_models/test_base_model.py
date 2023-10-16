#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime
from os.path import isfile


class BaseModelTest(TestCase):
    """
    Test cases for BaseModel class
    """

    def __init__(self):
        super().__init__()
        self.updated_at = datetime.now()

    def test_save(self):
        """
        Testing for save method
        """
        self.updated_at = datetime.now()
        model = BaseModel()
        updated = datetime.now()
        first = model.updated_at

        self.assertEqual(first.date(), model.updated_at.date())
        model.save()
        updated = datetime.now()
        second = model.updated_at
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
