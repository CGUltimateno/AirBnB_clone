#!/usr/bin/python3
"""
Unittest for State class
"""
from unittest import TestCase
from models.state import State
from datetime import datetime


class StateTest(TestCase):
    """
    Test cases for State class
    """

    def test_new_instance(self):
        """
        Testing for new instance
        """
        self.assertEqual(State.name, "")
