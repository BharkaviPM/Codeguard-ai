from services.groq_service import GroqService


class CodeChatService:

    @staticmethod
    def ask(code, review, question):

        prompt = f"""
You are CodeGuard AI.

Source Code:

{code}

Review Results:

{review}

Answer ONLY based on:

1. Uploaded code
2. Security findings
3. Code review findings

Question:

{question}
"""

        return GroqService.chat(prompt)