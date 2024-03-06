#!/usr/bin/python3
""" this is the test file for base_model. """
import unittest
form base.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """this class is for the class testing."""
    def setUp(self):
        """this is the setup for avoiding repeated instantiation"""
        self.model = BaseModel()

    def test_attributes(self):
        """testing the attr."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
