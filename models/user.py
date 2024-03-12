#!/usr/bin/python3
"""
this is the User class that implements user methods as the
task 8 demands.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ the user class that will hold data about those who use this console"""

    def __init__(self):
        """this is instantiation of the class attributes of user class"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
