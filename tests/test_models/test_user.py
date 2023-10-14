#!/usr/bin/python3
"""
Unittest for User class
"""
from unittest import TestCase
from models.user import User
from datetime import datetime
from os.path import isfile


class UserTest(TestCase):
    """
    Test cases for User class
    """

    def test_new_instance(self):
        """
        Testing for new instance
        """
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
