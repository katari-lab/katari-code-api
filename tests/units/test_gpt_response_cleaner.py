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

    def test_clean_testing_code(self):
        code = """\n```python\nimport unittest\nfrom .Customer import Customer\n\nclass TestCustomer(unittest.TestCase):\n    def test_full_name(self):\n        # Test with regular names\n        customer = Customer("John", "Doe")\n        result = customer.full_name()\n        self.assertEqual(result, "John Doe")\n        \n        # Test with names containing special characters\n        customer = Customer("Anne-Marie", "O\'Neill")\n        result = customer.full_name()\n        self.assertEqual(result, "Anne-Marie O\'Neill")\n        \n        # Test with names that have leading/trailing spaces\n        customer = Customer(" John", "Doe ")\n        result = customer.full_name()\n        self.assertEqual(result, " John Doe ")\n        \n        # Test with empty strings\n        customer = Customer("", "")\n        result = customer.full_name()\n        self.assertEqual(result, " ")\n        \n        # Test with numeric strings\n        customer = Customer("123", "456")\n        result = customer.full_name()\n        self.assertEqual(result, "123 456")\n\nif __name__ == \'__main__\':\n    unittest.main()\n```"""
        result = GptResponseCleaner.clean_code_response("test.py", code)
        code = """import unittest\nfrom .Customer import Customer\n\nclass TestCustomer(unittest.TestCase):\n    def test_full_name(self):\n        # Test with regular names\n        customer = Customer("John", "Doe")\n        result = customer.full_name()\n        self.assertEqual(result, "John Doe")\n        \n        # Test with names containing special characters\n        customer = Customer("Anne-Marie", "O\'Neill")\n        result = customer.full_name()\n        self.assertEqual(result, "Anne-Marie O\'Neill")\n        \n        # Test with names that have leading/trailing spaces\n        customer = Customer(" John", "Doe ")\n        result = customer.full_name()\n        self.assertEqual(result, " John Doe ")\n        \n        # Test with empty strings\n        customer = Customer("", "")\n        result = customer.full_name()\n        self.assertEqual(result, " ")\n        \n        # Test with numeric strings\n        customer = Customer("123", "456")\n        result = customer.full_name()\n        self.assertEqual(result, "123 456")\n\nif __name__ == \'__main__\':\n    unittest.main()"""
        self.assertEqual(result, code)


