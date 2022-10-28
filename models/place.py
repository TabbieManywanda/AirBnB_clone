#!/usr/bin/python3
"""place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    max_guest = 0
    price_by_night = 0
    number_of_rooms = 0
    number_of_bathrooms = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []