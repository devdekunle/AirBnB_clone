#!/usr/bin/python3
"""
This module contains the class that defines all common attributes/methods
for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This class creates the BaseModel class which acts as a super class for
    other classes to be used in the application
    """

    def __init__(self):
        """Method for object instantiation of the BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Method to make the instance printable"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method that updates the public instance attributes updated_at
        with the current datetime"""
        self.created_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/values of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
