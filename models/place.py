#!/usr/bin/python3
""" Module defines the class for the Place Model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """defines the State class that is a subclass of BaseModel"""

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []


    def __init__(self, *args, **kwargs):
        """Instantiates an object"""

        super().__init__(*args, **kwargs)
