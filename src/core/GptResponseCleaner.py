
import os

class GptResponseCleaner:

    @staticmethod
    def clean_code_response(filename: str, response: str) -> str:
        code_block_delimiter = "```"
        _, extension = os.path.splitext(filename)
        extension = extension.lstrip(".")
        language_block = ""

        if extension == "py":
            language_block = "python"
        elif extension == "txt":
            language_block = "plaintext"
        elif extension == "js":
            language_block = "javascript"
        else:
            language_block = "unknown"

        cleaned_code = response.replace(f"{code_block_delimiter}{language_block}", "")
        if cleaned_code.endswith(code_block_delimiter):
            cleaned_code = cleaned_code[:-len(code_block_delimiter)]
        
        cleaned_code = cleaned_code.lstrip("\n")
        cleaned_code = cleaned_code.rstrip("\n")
        return cleaned_code
