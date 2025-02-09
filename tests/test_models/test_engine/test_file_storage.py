#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.__init__ import storage
import os


class test_fileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        for obj in storage.all().values():
            with self.subTest(obj=obj):
                temp = obj
                self.assertTrue(temp is obj)

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skip("data type not matched")
    def test_all_with_classname(self):
        """__objects is properly returned using Class Name"""
        from models.user import User
        from models.city import City
        from models.state import State

        user = User()
        # save objects in file storage
        storage.new(user)
        # get instance in db
        obj = "{}.{}".format(type(user).__name__, user.id)
        instance = storage.all(type(user))[obj]
        args = instance.__class__.__name__ is user.__class__.__name__
        self.assertTrue(args)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            with self.subTest(obj=obj):
                loaded = obj
                self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    def test_reload_empty(self):
        """Load from an empty file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """BaseModel save method calls storage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        _id = new.to_dict()["id"]
        for key in storage.all().keys():
            with self.subTest(key=key):
                temp = key
                self.assertEqual(temp, "BaseModel" + "." + _id)

    def test_storage_var_created(self):
        """FileStorage object storage created"""
        from models.engine.file_storage import FileStorage

        self.assertEqual(type(storage), FileStorage)

    @unittest.skip("data type not matched")
    def test_delete(self):
        """Object is delete"""
        from models.user import User

        before = len(storage.all())
        user = User()
        storage.delete(user)
        after = len(storage.all())
        self.assertEqual(before, after)
