import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test environment
        """
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """
        Cleans up the test environment
        """
        self.storage.reload()

    def test_create_with_valid_params(self):
        """
        Test creating an object with valid parameters
        """
        command = HBNBCommand()
        args = "BaseModel name=\"Test Model\" number=123"
        command.do_create(args)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertEqual(self.storage.all()[0].name, "Test Model")
        self.assertEqual(self.storage.all()[0].number, 123)