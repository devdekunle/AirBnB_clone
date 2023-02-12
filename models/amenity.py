#!/usr/bin/python3
""" Module defines the class for the Amenity Model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines the State class that is a subclass of BaseModel"""

    name = ""


    def __init__(self, *args, **kwargs):
        """Instantiates an object"""

        super().__init__(*args, **kwargs)
