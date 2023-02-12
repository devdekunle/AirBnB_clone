#!/usr/bin/python3
""" Module defines the class for the Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """defines the State class that is a subclass of BaseModel"""

    text = ""
    place_id = ""
    user_id = ""


    def __init__(self, *args, **kwargs):
        """Instantiates an object"""

        super().__init__(*args, **kwargs)
