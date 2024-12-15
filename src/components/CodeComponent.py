from ..gateways.GPTGateway import GPTGateway
from ..core.GptResponseCleaner import GptResponseCleaner


class CodeComponent:

    def __init__(self):
        self.gpt_gateway = GPTGateway()

    def lint_code(self,filename: str, document: str):
        response = self.gpt_gateway.ask_llm(
            system="""
            You are a system expert that improves code without changing its behavior.
            Do not change class or method names.
            Do not modify the values within quotes or replace functions.
            Improve naming, fix typos, and enhance logic descriptions.
            Just return the improved code without a natural language explanation.
            If you find a comment starting with #> you must implement the functionality in the commend bellow that mark.
            """,
            prompt=document,
            temperature=0.3,
        )
        return GptResponseCleaner.clean_code_response(filename, document)
        