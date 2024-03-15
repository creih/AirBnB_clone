#!/usr/bin/python3
"""
this is the test file for base_model. and it has methods for different
functionalities of base_model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


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
        """this test is for if created_at and updated at where initialised"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_serialization_deserialization(self):
        """this is the serialisation tests """
        obj = BaseModel()
        serialized_obj = obj.to_dict()
        deserialized_obj = BaseModel(**serialized_obj)
        self.assertEqual(obj.__dict__, deserialized_obj.__dict__)

    def test_equality(self):
        """test if two instances are not that equal."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_instantiation(self):
        """ Test with and without keyword arguments"""
        instance1 = BaseModel()
        self.assertIsNotNone(instance1.id)
        self.assertIsNotNone(instance1.created_at)
        self.assertNotEqual(instance1.created_at, instance1.updated_at)

        timestamp = "2023-11-21T15:30:00.000000"
        kwargs = {"created_at": timestamp, "updated_at": timestamp}
        instance2 = BaseModel(**kwargs)
        self.assertEqual(
                instance2.created_at,
                datetime.fromisoformat(timestamp)
                )
        self.assertEqual(
                instance2.updated_at,
                datetime.fromisoformat(timestamp)
                )

    def test_save(self):
        """this test is for the save() method if it actually saves"""
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, original_updated_at)

    def test_to_dict(self):
        """testing for the to_dict() method for how it renders data"""
        instance = BaseModel(name="John Doe")
        data = instance.to_dict()
        self.assertEqual(data["__class__"], "BaseModel")
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
