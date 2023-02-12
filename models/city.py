#!/usr/bin/python3
""" Module defines the class for the city Model"""

from models.base_model import BaseModel


class City(BaseModel):
    """defines the State class that is a subclass of BaseModel"""

    state_id = ""
    name = ""


    def __init__(self, *args, **kwargs):
        """Instantiates an object"""

        super().__init__(*args, **kwargs)
