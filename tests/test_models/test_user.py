#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
import unittest

from models.user import User

from models import storage

if type(storage).__name__ == "FileStorage":
    RUN_TEST = False
else:
    RUN_TEST = True
skip_msg = "DB storage does'nt have this type of fields"


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(not RUN_TEST, skip_msg)
    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(not RUN_TEST, skip_msg)
    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(not RUN_TEST, skip_msg)
    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(not RUN_TEST, skip_msg)
    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
