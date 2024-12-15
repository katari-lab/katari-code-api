import unittest
from src.core.GptResponseCleaner import GptResponseCleaner


class TestGptResponseCleaner(unittest.TestCase):

    def test_clean_code_response_with_python_file(self):
        filename = "example.py"
        response = "```python\nprint('Hello, World!')\n```"
        expected_output = "\nprint('Hello, World!')\n"
        
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_with_non_python_file(self):
        filename = "example.txt"
        response = "```plaintext\nSome text content\n```"
        expected_output = "\nSome text content\n"
        
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_with_partial_code_block(self):
        filename = "example.py"
        response = "```python\nprint('Hello, World!')"
        expected_output = "\nprint('Hello, World!')"
        
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

