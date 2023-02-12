#!/usr/bin/python3
""" Module that serializes instances to json file and deserialzes json file
to instances"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State

class FileStorage:
    """ Module that serializes instances to json file and deserialzes json file
    to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary of all __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """store Class instances in FileStorage.__objects dictionary"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes objects to the json file"""
        new_dict = {}
        for key in FileStorage.__objects:
            inst_dict = FileStorage.__objects[key].to_dict()
            new_dict[key] = inst_dict
        with open("file.json", "w") as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """deserializes the json file to only if the file exists"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as my_file:
                json_dict = json.load(my_file)
                for dict_val in json_dict.values():
                    class_name = dict_val["__class__"]
                    del dict_val["__class__"]
                    self.new(eval(class_name)(**dict_val))
