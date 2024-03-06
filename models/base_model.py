#!/usr/bin/python3
"""
this is the base file for the whole project
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    this class is the base class for the whole project
    """
    def __init__(self):
        """ this is the initiation of BaseModel class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.onw()
        self.updated_at = datetime.now()

    def __str__(self):
        """ this is the string representation of BaseModel """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ this ought to be the save file that changes update at time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary to store class name and attributes"""
        obave = self.__dict__.copy()
        obave['__class__'] = self.__class__.__name__
        obave['created_at'] = self.created_at.isoformat()
        obave['updated_at'] = self.updated_at.isoformat()
        return obave
