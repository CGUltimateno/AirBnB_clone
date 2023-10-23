#!/usr/bin/python3
"""
Module for the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The user class from which future user objects will be derived
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
