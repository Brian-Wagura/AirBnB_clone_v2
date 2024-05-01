from io import StringIO
import unittest
from console import HBNBCommand
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestDoCreateCommand(unittest.TestCase):
    """
    Test cases for the do_create() function
    """

    def setUp(self):
        """
        Sets up the test environment
        """
        self.console = HBNBCommand()
        self.storage = FileStorage()
        self.storage.reload()

    def test_create_with_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_with_non_existent_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.do_create("NonExistentClass name=value")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_with_valid_string_parameter(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.do_create('User name="John Doe" email="john@example.com"')
            self.assertIn("User.", f.getvalue().strip())

    def test_create_with_valid_int_parameter(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.do_create("Amenity number_rooms=5")
            self.assertIn("Amenity.", f.getvalue().strip())

    def test_create_with_valid_float_parameter(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.do_create("Place latitude=10.0 longitude=20.0")
            self.assertIn("Place.", f.getvalue().strip())

    def test_create_with_missing_value(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.do_create('User name="John Doe" email=')
            self.assertIn("User.", f.getvalue().strip(), "** value missing **")
