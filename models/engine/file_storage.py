#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import datetime
import os
from os.path import isfile


def save():
    """
    Serializes __objects to the JSON file (path: __file_path)
    """
    with open(FileStorage.__file_path, "w") as f:
        f.write(json.dumps({k: v.to_dict()
                            for k, v in FileStorage.__objects.items()}))


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if not isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            for k, v in json.loads(f.read()).items():
                FileStorage.__objects[k] = self.classes()[v["__class__"]](**v)

    def classes(self):
        """
        Returns a dictionary of valid classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        return {"BaseModel": BaseModel, "User": User,
                "State": State, "City": City,
                "Amenity": Amenity, "Place": Place, "Review": Review}

    def attributes(self):
        """
        Returns a dictionary of valid attributes
        """
        return {
            "BaseModel": {"id": str,
                          "created_at": datetime.datetime,
                          "updated_at": datetime.datetime},
            "User": {"email": str, "password": str,
                     "first_name": str, "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str, "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str, "user_id": str,
                      "name": str, "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review": {"place_id": str, "user_id": str,
                       "text": str}
        }
