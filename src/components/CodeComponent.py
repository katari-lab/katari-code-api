from ..gateways.GPTGateway import GPTGateway
class CodeComponent:

    def __init__(self):
        self.gateway = GPTGateway()

    def code(self, document: str):
        response = self.gateway.question_llm(
            system="""
            your a system expert code that return improve code from the code that you receive without change the behavior.
            the code that you recommend must improve the naming, fix typos and logic description
            just return the better code without a natural language explanation
            """, prompt=document)
        text = response.choices[0].message.content
        text = text.replace("```python", "")
        if text[-3:]== "```":
            text = text[:-3]
        return text