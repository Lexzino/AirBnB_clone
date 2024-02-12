#!/usr/bin/python3
<<<<<<< HEAD
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
=======
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
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
