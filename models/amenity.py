#!/usr/bin/python3
"""
Amenity module.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity object.
        """
        super().__init__(*args, **kwargs)
