#!/usr/bin/python3
<<<<<<< HEAD
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
=======
"""
Unitest Class BaseModel
"""
import unittest
from models.base_model import BaseModel, __doc__ as mrdoc
import inspect
import pep8
import models
from datetime import datetime as datetime


class TestBaseModel(unittest.TestCase):
    """
    Unitest for testing
    """
    def test_module_docstring(self):
        """
        Tests docstring for module
        """
        self.assertTrue(len(mrdoc) > 20)

    def test_class_docstring(self):
        """
        Tests docstring for class
        """
        self.assertTrue(len(BaseModel.__doc__) > 20)

    def test_methods_docstring(self):
        """
        Tests docstring for methods
        """
        methods = inspect.getmembers(BaseModel, predicate=inspect.ismethod)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 20)
        methods = inspect.getmembers(BaseModel, predicate=inspect.isfunction)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 20)

    def test_docstring_for_test(self):
        """
        Tests docstring for this test
        """
        self.assertTrue(len(__doc__) > 20)

    def test_docstring_class_test(self):
        """
        Tests dosctring for class TestBaseModel
        """
        self.assertTrue(len(TestBaseModel.__doc__) > 20)

    def test_docstring_methods(self):
        """
        Tests docstring for all methods in TestBaseModel class
        """
        methods = inspect.getmembers(TestBaseModel, predicate=inspect.ismethod)
        for name, func in methods:
            self.assertTrue(len(func.__doc__) > 20)

    def test_pep8(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_base_init(self):
        """
        Testing a class BaseModel
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(issubclass(type(instance), BaseModel))
        self.assertIs(type(instance), BaseModel)

        instance.name = "Holberton"
        instance.my_number = 89
        self.assertEqual(instance.name, "Holberton")
        self.assertEqual(instance.my_number, 89)
        """
        at_class = {
            "id": str,
            "created_at": datetime
            "updated_at": datetime
            "name": str
            "my_number": int
        }
        """

    def test_none(self):
        """Check if a new instance is not none"""
        bm1 = BaseModel()
        self.assertIsNotNone(bm1)

    def test_uuid(self):
        """Check ids in the created instances"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at(self):
        """Check if the instance has created_at Atttibute"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm1, "created_at")
        self.assertTrue(bm2, "created_at")

    def test_updated_at(self):
        """Check if the instance has created_at Atttibute"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm1, "updated_at")
        self.assertTrue(bm2, "updated_at")

    def test__str__(self):
        """Check the string of an created instance"""
        bm1 = BaseModel()
        printed = "[{}] ({}) {}".format(
            bm1.__class__.__name__, bm1.id, bm1.__dict__)
        self.assertEqual(str(bm1), printed)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(str(bm1.id), bm1_dict["id"])
        self.assertIsInstance(bm1_dict["created_at"], str)
        self.assertIsInstance(bm1_dict["updated_at"], str)

    def test_save(self):
        """Test to check each update in the storage"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "updated_at"))
        bm1.save()
        self.assertTrue(hasattr(bm1, "updated_at"))
        t_arg = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                 'create_at': datetime(2017, 9, 28, 21, 5, 54, 119427),
                 'updated_at': datetime(2017, 9, 28, 21, 5, 54, 119572),
                 'name': 'bm1'}
        bm2 = BaseModel(t_arg)
        bm2.save()
        last_time = bm2.updated_at
        bm2.save()
        self.assertNotEqual(last_time, bm2.updated_at)

    def test_init_from_dict(self):
        """test to check a new instance witk Kwargs"""
        my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        bm1 = BaseModel(**my_dict)
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm1.id, str)
        self.assertEqual(bm1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertIsInstance(bm1.name, str)
        self.assertEqual(bm1.name, 'Holberton')
        self.assertEqual(
            bm1.created_at.isoformat(), '2017-09-28T21:03:54.052298')
        self.assertEqual(
            bm1.updated_at.isoformat(), '2017-09-28T21:03:54.052302')

    def test_new_attributte(self):
        """test to check if new attribute  can be added"""
        bm1 = BaseModel()
        bm1.name = "Betty"
        self.assertEqual(bm1.name, "Betty")
>>>>>>> 07d301bcc0720ce90bcdb7669deb9c857fd9da91
