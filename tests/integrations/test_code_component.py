
import unittest
from src.components.CodeComponent import CodeComponent
from ..common import load_ini_and_set_env

class CodeComponentTest(unittest.TestCase):
    
    def setUp(self):
        load_ini_and_set_env()
        super().setUp()
    
    def test_invalid_python_code(self):
        code_snippet = """
        def function(self):
            1 = 2
        """
        result = CodeComponent().code(code_snippet)
        self.assertTrue(result)
        print(result)
