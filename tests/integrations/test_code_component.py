import unittest
from src.components.CodeComponent import CodeComponent
from ..common import load_ini_and_set_env
class CodeComponentTest(unittest.TestCase):
    def setUp(self):
        load_ini_and_set_env()
        return super().setUp()
    
    def test_python(self):
        c = """
        def function(self):
            1 = 2
        """
        result = CodeComponent().code(c)
        self.assertTrue(result)