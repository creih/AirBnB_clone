#!/usr/bin/python3
"""
this is the test for user class in models module
"""
from unittest import TestCase
from models.user import User


class Test_user(TestCase):
    """
    this class encloses all methods that will
    be used to test the user class really
    """

    def atts_are_str(self):
        """this method checks if email i a string"""
        user_o = User()
        self.assertIsInstance(user_o.email, str)
        self.assertIsInstance(user_o.password, str)
        self.assertIsInstance(user_o.first_name, str)
        self.assertIsInstance(user_o.last_name, str)


if __name__ == '__main__':
    unittest.main()
