import unittest
from src.components.CodeComponent import CodeComponent
from ..common import load_ini_and_set_env


class TestCodeComponent(unittest.TestCase):

    def setUp(self):
        load_ini_and_set_env()
        super().setUp()

    def test_invalid_python_code(self):
        code_snippet = """
        def function(self):
            1 = 2
        """
        result = CodeComponent().code(code_snippet)
        self.assertFalse(result)  # > The test should assert False for invalid code
        print(result)

    def test_valid_python_code(self):
        code_snippet = """
        def function(self):
            return 1 + 2
        """
        result = CodeComponent().code(code_snippet)
        self.assertTrue(result)
