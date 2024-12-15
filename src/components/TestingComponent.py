
from ..gateways.GPTGateway import GPTGateway
from ..core.GptResponseCleaner import GptResponseCleaner

class TestingComponent:

    def __init__(self):
        self.gpt_gateway = GPTGateway()

    def create_unit_test(self, filename: str, document: str):
        response = self.gpt_gateway.ask_llm(
            system="""
            You are an expert system that creates unit test code for the provided code.
            """,
            prompt=document,
            temperature=0.5,
        )
        unit_test_code = response.choices[0].message.content
        return GptResponseCleaner.clean_code_response(filename, unit_test_code)
