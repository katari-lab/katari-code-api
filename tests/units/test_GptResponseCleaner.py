import unittest
from src.core.GptResponseCleaner import GptResponseCleaner

class TestGptResponseCleaner(unittest.TestCase):

    def test_clean_code_response_python(self):
        filename = "example.py"
        response = "\nprint('Hello, World!')\n```"
        expected_output = "print('Hello, World!')"
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_plaintext(self):
        filename = "example.txt"
        response = "```plaintext\nThis is a plain text.\n```"
        expected_output = "This is a plain text."
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_no_language_block(self):
        filename = "example.py"
        response = "print('Hello, World!')"
        expected_output = "print('Hello, World!')"
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_with_extra_newlines(self):
        filename = "example.py"
        response = "\n\nprint('Hello, World!')\n\n```"
        expected_output = "print('Hello, World!')"
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_other_extension(self):
        filename = "example.js"
        response = "```javascript\nconsole.log('Hello, World!');\n```"
        expected_output = "console.log('Hello, World!');"
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_missing_delimiter(self):
        filename = "example.py"
        response = "python\nprint('Hello, World!')"
        expected_output = "python\nprint('Hello, World!')"
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_incorrect_extension(self):
        filename = "example.unknown"
        response = "```unknown\nUnknown content\n```"
        expected_output = "Unknown content"
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

    def test_clean_code_response_empty_response(self):
        filename = "example.py"
        response = ""
        expected_output = ""
        result = GptResponseCleaner.clean_code_response(filename, response)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()