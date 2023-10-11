#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from json import dumps, loads
from os.path import isfile

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

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as f:
            f.write(dumps({k: v.to_dict() for k, v in FileStorage.__objects.items()}))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        objs = {}
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                objects = loads(file.read())
            from models.base_model import BaseModel
            for key, value in objects.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
