#!/usr/bin/python3
""" this is the test file for base_model. """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """this class is for the class testing."""
    def setUp(self):
        """this is the setup for avoiding repeated instantiation"""
        self.model = BaseModel()

    def test_init_attributes(self):
        """testing if the attributes are of correct data type."""
        self.assertIsInstance(self.model.id, str)
        '''self.assertIsInstance(self.model.created_at, datetime)'''
        '''f.assertIsInstance(self.model.updated_at, datetime)'''

    def test_str_method(self):
        """ test the str method """
        exp_str = "[BaseModel] ({}) {}".format(
                self.model.id,
                self.model.__dict__
                )
        self.assertEqual(str(self.model), exp_str)
