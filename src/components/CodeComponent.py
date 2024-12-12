
from ..gateways.GPTGateway import GPTGateway

class CodeComponent:

    def __init__(self):
        self.gpt_gateway = GPTGateway()

    def code(self, document: str):
        code_block_delimiter = "```"
        response = self.gpt_gateway.ask_llm(
            system="""
            You are a system expert that improves code without changing its behavior.
            Do not change class or method names.
            Do not modify the values within quotes or replace functions.
            Improve naming, fix typos, and enhance logic descriptions.
            Just return the improved code without a natural language explanation.
            """, 
            prompt=document,
            temperature=0.3
        )
        improved_code = response.choices[0].message.content
        improved_code = improved_code.replace(f"{code_block_delimiter}python", "")
        if improved_code.endswith(code_block_delimiter):
            improved_code = improved_code[:-3]
        return improved_code
