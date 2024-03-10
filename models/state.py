#!/usr/bin/python3
"""this class is for the state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes State object.
        """
        super().__init__(*args, **kwargs)
