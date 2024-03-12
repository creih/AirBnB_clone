#!/usr/bin/python3
"""
this is the User class that implements user methods as the
task 8 demands.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ the user class that will hold data about those who use this console"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
