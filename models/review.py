#!/usr/bin/python3
"""
Review module.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Review object.
        """
        super().__init__(*args, **kwargs)
