#!/usr/bin/python3
"""
this is the base file for the whole project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    this class is the base class for the whole project
    """
    def __init__(self, *args, **kwargs):
        """ this is the initiation of BaseModel class """
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'],
                        "%Y-%m-%dT%H:%M:%S.%f"
                        )
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'],
                        "%Y-%m-%dT%H:%M:%S.%f"
                        )
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ this is the string representation of BaseModel """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """ this ought to be the save file that changes update at time"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """
        dictionary to store class name and attributes and
        obave stands in as copy of __dict__ 's object
        """
        obave = self.__dict__.copy()
        obave['__class__'] = self.__class__.__name__
        obave['updated_at'] = self.updated_at.isoformat()
        obave['created_at'] = self.created_at.isoformat()
        return obave
