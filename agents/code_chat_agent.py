from services.groq_service import GroqService


class CodeChatAgent:

    @staticmethod
    def ask(code, question):

        prompt = f"""
You are a senior software engineer.

Code:

{code}

Question:

{question}

Answer with:

- exact line number
- explanation
- fix
"""

        return GroqService.chat(prompt)