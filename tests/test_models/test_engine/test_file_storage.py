#!/usr/bin/python3
"""
Unitest class File_Storage
"""
import unittest
import json
import pep8
import os.path
from models.engine.file_storage import FileStorage, __doc__ as mrdoc
import inspect
from models.base_model import BaseModel
my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
           'created_at': '2017-09-28T21:03:54.052298',
           '__class__': 'BaseModel', 'my_number': 89,
           'updated_at': '2017-09-28T21:03:54.052302',
           'name': 'Holberton'}


class TestFileStorage(unittest.TestCase):
    """
    Unittest for file_storage.py
    """
    storage = FileStorage()
    path = storage._FileStorage__file_path
    bm_instance = BaseModel(**my_dict)
    storage.new(bm_instance)

    def test_module_docstring(self):
        """
        Tests docstring for module
        """
        self.assertTrue(len(mrdoc) > 20)

    def test_methods_docstring(self):
        """
        Tests docstring for methods
        """
        methods = inspect.getmembers(FileStorage, predicate=inspect.ismethod)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 20)
        methods = inspect.getmembers(FileStorage, predicate=inspect.isfunction)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 20)

    def test_pep8(self):
        """
        Tests for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_for_test(self):
        """
        Tests docstring for this test
        """
        self.assertTrue(len(__doc__) > 20)

    def test_docstring_class_test(self):
        """
        Tests dosctring for class TestBaseModel
        """
        self.assertTrue(len(TestFileStorage.__doc__) > 20)

    def test_docstring_methods(self):
        """
        Tests docstring for all methods in TestBaseModel class
        """
        methods = inspect.getmembers(
            TestFileStorage, predicate=inspect.ismethod)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 20)

    def test_storage_isinstance(self):
        """
        Tests if storage is an instance of FileStorage
        """
        self.assertIsInstance(TestFileStorage.storage, FileStorage)

    def test_file_json(self):
        """
        Tests for path existence
        """
        TestFileStorage.storage.save()
        self.assertTrue(os.path.exists(TestFileStorage.path))

    def test_reload(self):
        """
        Test for instances reloaded from path
        """
        key = my_dict["__class__"] + "." + my_dict["id"]
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        attributes = reader[key]
        self.assertEqual(my_dict, attributes)
        self.assertIsInstance(TestFileStorage.storage.all()[key], BaseModel)

    def test_save_another_instance(self):
        """
        Tests for save another instance in path
        """
        bm2_instance = BaseModel()
        bm2_instance.save()
        key = type(bm2_instance).__name__ + "." + str(bm2_instance.id)
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        self.assertEqual(
            reader[key], TestFileStorage.storage.all()[key].to_dict())

if __name__ == '__main__':
    pass
