#!/usr/bin/python3
""" Module that contains the class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class is a subclass of the BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates an object of the User class"""
        super().__init__(*args, **kwargs)
