#!/usr/bin/python3
"""class FileStorage that serializes instances
to a JSON file and deserializes JSON file to
instances"""
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with
        key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file
        (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    ForStorage.__objects[key] = eval(val["__class__"])(**val)
