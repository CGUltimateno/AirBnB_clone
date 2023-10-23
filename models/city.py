#!/usr/bin/python3
"""
Module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class from which future City objects will be derived
    """
    state_id = ""
    name = ""
