#!/usr/bin/python3
"""this is the actual and famous module for user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """the actual user instance inheriting the basmodel class """

    def __init__(self):
        """the initialisation of user class happens here to those wondering"""
        super().__init__(self, *ars, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
