#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    Base class for all models in our hbnb clone
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation of a new model
        """
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, datetime.fromisoformat(value)
                if ("_at" in key) else value)

    def __str__(self):
        """
        String representation of the BaseModel class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        obj = {}

        for key, value in self.__dict__.items():
            obj[key] = value.isoformat() if ("_at" in key) else value
        obj["__class__"] = type(self).__name__
        return obj
