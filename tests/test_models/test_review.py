#!/usr/bin/python3
"""
Unittest for Review class
"""
from unittest import TestCase
from models.review import Review
from datetime import datetime


class ReviewTest(TestCase):
    """
    Test cases for Review class
    """

    def test_new_instance(self):
        """
        Testing for new instance
        """
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
