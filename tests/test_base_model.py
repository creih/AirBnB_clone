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
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """ test the str method """
        exp_str = "[BaseModel] ({}) {}".format(
                self.model.id,
                self.model.__dict__
                )
        self.assertEqual(str(self.model), exp_str)

    def test_initialization(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_serialization_deserialization(self):
        obj = BaseModel()
        serialized_obj = obj.to_dict()
        deserialized_obj = BaseModel(**serialized_obj)
        self.assertEqual(obj.__dict__, deserialized_obj.__dict__)

    def test_attribute_modification(self):
        obj = BaseModel()
        obj.name = "Test"
        self.assertEqual(obj.name, "Test")

    def test_equality(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_validation(self):
        obj = BaseModel()
        obj.name = 123
        self.assertNotEqual(obj.name, 123)

    def test_edge_cases(self):
        obj = BaseModel()
        obj.name = ""
        self.assertEqual(obj.name, "")

if __name__ == '__main__':
    unittest.main()
