
from ..gateways.GPTGateway import GPTGateway
from ..core.GptResponseCleaner import GptResponseCleaner

class TestingComponent:

    def __init__(self):
        self.gpt_gateway = GPTGateway()

    def create_unit_test(self, filename: str, document: str):
        separator = "*" * 55
        response = self.gpt_gateway.ask_llm(
            system=f"""
            You are an expert system that creates unit test code for the python provided code.
            You will receive the source code under the test and the existing test code.
            You can not modify the source code under the test and that can not be part of your response.
            Your response must consider the existing test code and update with your recommendations.
            For example: 
            class Demo:
                def action(self, a , b):
                    return a + b
            {separator}
            import unittest
            from .Demo import Demo
            class TestDemo(unittest.TestCase):
                def test_action(self):
                    target = Demo()
                    result = target.action(1, 2)
                    self.assertEqual(result, 3)
            """,
            prompt=document,
            temperature=0.5,
        )
        unit_test_code = response.choices[0].message.content
        return GptResponseCleaner.clean_code_response(filename, unit_test_code)
