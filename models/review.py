#!/usr/bin/python3
"""
Module for the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class from which future Review objects will be derived
    """
    place_id = ""
    user_id = ""
    text = ""
